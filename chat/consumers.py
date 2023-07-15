from channels.generic.websocket import AsyncWebsocketConsumer


class MyWebSocket(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data)