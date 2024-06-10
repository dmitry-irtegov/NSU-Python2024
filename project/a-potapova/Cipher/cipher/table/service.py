import asyncio

from fastapi import status

from cipher.core.entity.language import Language
from cipher.core.service import CipherService
from cipher.table.cipher import TableCipher
from cipher.table.decrypter import FrequencyDecrypter
from cipher.table.entity.key import TableKey
from cipher.table.entity.text import TableText


class TableCipherService(CipherService):
    def __init__(self):
        self.cipher = TableCipher
        self.decrypter: FrequencyDecrypter = FrequencyDecrypter()
        self.task = None
        self.result: tuple[str, str, status] = None

    def keygen(self, language: str, **kwargs) -> str:
        language = Language(language)
        return str(self.cipher.keygen(language))

    def encode(self, plaintext: str, key: str = None) -> str:
        text = TableText(plaintext)
        if key is None or key == "":
            ciphertext = text
        else:
            table_key = TableKey(key)
            ciphertext = self.cipher.encrypt(text, key=table_key)
        print(ciphertext)
        return str(ciphertext)

    async def decode(self, ciphertext: str, timeout: float, key: str = None) -> tuple[str, str, status]:
        self.task = None
        self.result = None
        text = TableText(ciphertext)
        if key is None or key == "":
            self.task = asyncio.create_task(asyncio.wait_for(self.decrypter.decode(text),
                                                             timeout=timeout))
            try:
                plaintext, table_key, result_status = await self.task
            except (asyncio.TimeoutError, asyncio.CancelledError):
                plaintext, table_key, result_status = await self.read()
        else:
            table_key = TableKey(key)
            plaintext = TableCipher.decrypt(text, key=table_key)
            result_status = status.HTTP_200_OK
        self.result = str(plaintext), str(table_key), result_status
        return self.result

    async def read(self) -> tuple[str, str, status]:
        if self.result is None:
            plaintext, table_key, result_status = await self.decrypter.get_current_result()
            self.result = str(plaintext), str(table_key), result_status
        return self.result

    async def stop(self) -> tuple[str, str, status]:
        if self.task is not None:
            try:
                self.task.cancel()
            except (asyncio.TimeoutError, asyncio.CancelledError):
                plaintext, table_key, result_status = self.decrypter.get_current_result()
                self.result = str(plaintext), str(table_key), result_status
        return await self.read()
