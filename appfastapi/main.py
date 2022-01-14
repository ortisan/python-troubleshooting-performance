from fastapi import FastAPI, Depends
from prometheus_fastapi_instrumentator import Instrumentator
from typing import List
from database import TickModel, get_db, Tick

app = FastAPI()

# Instrumentalize api and expose /metrics endpoint
Instrumentator().instrument(app).expose(app)

@app.get("/", response_model=List[TickModel], dependencies=[Depends(get_db)])
# @app.get("/", dependencies=[Depends(get_db)])
async def get_all():
    ticks = (Tick
                .select()
                .order_by(Tick.epoch_timestamp.desc()))

    print(ticks)
    ticks_response = [TickModel.from_orm(tick) for tick in ticks]
    return list(ticks_response)