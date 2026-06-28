import asyncio
import json

import pytest
import websockets

API_URL = "ws://127.0.0.1:8765/"


async def _mock_realtime_server(websocket):
    subscribe_message = json.loads(await websocket.recv())
    assert subscribe_message["action"] == "subscribe"

    await websocket.send(
        json.dumps(
            {
                "status": "success",
                "subscribed_to": subscribe_message["channel"],
            }
        )
    )

    for index in range(3):
        await websocket.send(
            json.dumps(
                {
                    "timestamp": f"2026-06-27T00:00:0{index}",
                    "payload_data": {"index": index},
                }
            )
        )


def test_realtime_websocket_communication():
    """Tests a realtime websocket flow using a local mock server."""

    async def run_test():
        async with websockets.serve(_mock_realtime_server, "127.0.0.1", 8765):
            async with websockets.connect(API_URL) as websocket:
                subscribe_message = {
                    "action": "subscribe", "channel": "live_updates"}
                await websocket.send(json.dumps(subscribe_message))

                ack_response = json.loads(await asyncio.wait_for(websocket.recv(), timeout=5))
                assert ack_response.get("status") == "success"
                assert ack_response.get("subscribed_to") == "live_updates"

                messages_received = []
                for _ in range(3):
                    data = json.loads(await asyncio.wait_for(websocket.recv(), timeout=5))
                    messages_received.append(data)

                assert len(messages_received) == 3
                for message in messages_received:
                    assert "timestamp" in message
                    assert "payload_data" in message

    asyncio.run(run_test())
