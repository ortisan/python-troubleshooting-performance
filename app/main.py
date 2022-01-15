from fastapi import FastAPI, Depends
from prometheus_fastapi_instrumentator import Instrumentator
from typing import List
from database import TickModel, get_db, Tick
import logging as log

app = FastAPI()

# Instrumentalize api and expose /metrics endpoint
Instrumentator().instrument(app).expose(app)

@app.get("/", response_model=List[TickModel], dependencies=[Depends(get_db)])
async def get_all():
    
    log.info('Request received...')
    
    ticks = (Tick
                .select()
                .order_by(Tick.epoch_timestamp.desc()))

    ticks_response = [TickModel.from_orm(tick) for tick in ticks]
    
    log.info('Response: ', ticks_response)

    return ticks_response

