from fastapi import APIRouter

router = APIRouter()

@router.post("/create_new_table")
async def create_new_table():
    return 'not implemented yet'

@router.post("/add_column")
async def add_column():
    return 'not implemented yet'

@router.post("/add_item")
async def add_item(items:dict):
    return 'not implemented yet'

@router.get("/table_info")
async def table_info(table_name:str):
    columns = [
        'project_id',
        'project_name',
        'project_description',
        'address',
        'city',
        'state',
        'zipcode',
        'start_date',
        'end_date',
        'duration',
        'total_cost',
        'budget',
        'expenses',
        'contractor_name',
        'contractor_contact',
        'materials_used',
        'products_used',
        'rooms',
        'room_dimensions',
        'status',
        'progress_notes',
        'images',
        'documents',
        'warranty_expiration',
        'notes',
        'categories'
    ]
    return columns


@router.get("/table_info_all_tables")
async def table_info_all_tables():
    return 'not implemented yet'

@router.get("/latest_items")
async def latest_items():
    return 'not implemented yet'

@router.delete("/delete_column")
async def delete_column():
    return 'not implemented yet'

@router.delete("/delete_item")
async def delete_item():
    return 'not implemented yet'

@router.delete("/delete_table")
async def delete_row():
    return 'not implemented yet'
