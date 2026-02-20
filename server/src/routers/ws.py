from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import time
import asyncio
import queue
import threading

router = APIRouter()
start_time = time.time()

def read_loop(eeg, sample_queue, stop_event):
    while not stop_event.is_set():
        sample = eeg.read_sample()
        if sample is not None:
            sample_queue.put(sample)

@router.websocket("/eeg-ws")
async def eeg_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    eeg = websocket.app.state.eeg

    sample_queue = queue.Queue()
    stop_event = threading.Event()
    thread = threading.Thread(target=read_loop, args=(eeg, sample_queue, stop_event), daemon=True)
    thread.start()

    try:
        while True:
            if not sample_queue.empty():
                sample = sample_queue.get()
                await websocket.send_json({
                    "timestamp": round(time.time() - start_time, 4),
                    "sample": sample
                })
            else:
                await asyncio.sleep(0.001)
    except WebSocketDisconnect:
        print("Browser has disconnected normally.")
    except KeyBoardInterrupt:
        print("Keyboard Interrupted...")
    finally:
        stop_event.set()
