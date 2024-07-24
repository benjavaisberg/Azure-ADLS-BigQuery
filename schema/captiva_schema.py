from google.cloud import bigquery

deliveries_by_date_schema = [
    bigquery.SchemaField("Internal_Doc", "STRING"),
    bigquery.SchemaField("From_Whse", "STRING"),
    bigquery.SchemaField("Doc_Num", "STRING"),
    bigquery.SchemaField("Doc_Date", "STRING"),
    bigquery.SchemaField("Creation_Time", "STRING"),
    bigquery.SchemaField("Item_No", "STRING"),
    bigquery.SchemaField("Item_Description", "STRING"),
    bigquery.SchemaField("Quantity", "FLOAT"),
    bigquery.SchemaField("UoM_Code", "STRING"),
    bigquery.SchemaField("Units_Per_Pallet", "FLOAT"),
    bigquery.SchemaField("Pallet_Qty", "FLOAT"),
    bigquery.SchemaField("Remarks", "STRING"),
    bigquery.SchemaField("Batch_Number", "STRING"),
    bigquery.SchemaField("Created_By", "STRING")
]

receipt_resin_preforms_schema = [
    bigquery.SchemaField("Internal_Doc", "STRING"),
    bigquery.SchemaField("To_Whse", "STRING"),
    bigquery.SchemaField("Doc_No", "STRING"),
    bigquery.SchemaField("Doc_Date", "STRING"),
    bigquery.SchemaField("Creation_Time", "STRING"),
    bigquery.SchemaField("Item_No", "STRING"),
    bigquery.SchemaField("Item_Description", "STRING"),
    bigquery.SchemaField("Quantity", "FLOAT"),
    bigquery.SchemaField("UoM_Code", "STRING"),
    bigquery.SchemaField("Units_Per_Pallet", "FLOAT"),
    bigquery.SchemaField("Pallet_Qty", "FLOAT"),
    bigquery.SchemaField("Remarks", "STRING"),
    bigquery.SchemaField("Batch_Number", "STRING"),
    bigquery.SchemaField("Created_By", "STRING")
]

warehouse_transfers_schema = [
    bigquery.SchemaField("From_Whse", "STRING"),
    bigquery.SchemaField("To_Whse", "STRING"),
    bigquery.SchemaField("Doc_No", "STRING"),
    bigquery.SchemaField("Doc_Date", "STRING"),
    bigquery.SchemaField("Create_Time", "STRING"),
    bigquery.SchemaField("Item_No", "STRING"),
    bigquery.SchemaField("Item_Description", "STRING"),
    bigquery.SchemaField("Quantity", "FLOAT"),
    bigquery.SchemaField("UoM_Code", "STRING"),
    bigquery.SchemaField("Bottels_Per_Pallet", "FLOAT"),
    bigquery.SchemaField("Pallet_Qty", "FLOAT"),
    bigquery.SchemaField("Remarks", "STRING"),
    bigquery.SchemaField("Batch_Number", "STRING"),
    bigquery.SchemaField("Created_by", "STRING")
]

sales_order_forecast_schema = [
    bigquery.SchemaField("ShippingDate", "STRING"),
    bigquery.SchemaField("ShippingType", "STRING"),
    bigquery.SchemaField("Customer", "STRING"),
    bigquery.SchemaField("CustomerName", "STRING"),
    bigquery.SchemaField("SONo", "STRING"),
    bigquery.SchemaField("SODate", "STRING"),
    bigquery.SchemaField("SOStatus", "STRING"),
    bigquery.SchemaField("CustRefNo", "STRING"),
    bigquery.SchemaField("InternalStatus", "STRING"),
    bigquery.SchemaField("Carrier", "STRING"),
    bigquery.SchemaField("Pallets", "FLOAT"),
    bigquery.SchemaField("Cases", "FLOAT"),
    bigquery.SchemaField("Boxes", "FLOAT"),
    bigquery.SchemaField("Bags", "FLOAT"),
    bigquery.SchemaField("Bottles", "FLOAT"),
    bigquery.SchemaField("CAPS", "FLOAT"),
    bigquery.SchemaField("CoCStatus", "STRING"),
    bigquery.SchemaField("SalesEmployee", "STRING")
]

inventory = [
    bigquery.SchemaField("BinCode", "STRING"),
    # bigquery.SchemaField("ItemCode", "STRING"),
    bigquery.SchemaField("PalletQty", "FLOAT"),
    bigquery.SchemaField("Timestamp", "TIMESTAMP"),
]
