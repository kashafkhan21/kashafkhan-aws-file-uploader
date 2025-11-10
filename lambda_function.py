import json
import boto3
import base64
import uuid

s3 = boto3.client("s3")
BUCKET_NAME = "kashafbucket-10nov2025"  # <-- replace this

def lambda_handler(event, context):
    try:
        # check if body exists
        if "body" not in event or not event["body"]:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No file data received"})
            }

        # decode image
        file_content = base64.b64decode(event["body"])
        file_name = f"upload-{uuid.uuid4()}.jpg"

# --- DYNAMODB WRITE INSTRUCTIONS START HERE ---
        
        # 1. Initialize DynamoDB
        dynamodb = boto3.resource('dynamodb')
        
        # 2. Reference your specific table
        # !!! REPLACE 'kashaftable-10nov2025' with your actual table name if it's different
        table = dynamodb.Table('kashaftable-10nov2025') 
        
        # 3. Define the item to save
        # Note: 'id' must match your table's Partition Key!
        item_data = {
            'id': str(uuid.uuid4()),      # Creates a unique ID for the database entry
            'FileKey': file_name,         # The name under which the file was saved in S3 (from Line 21)
            'BucketName': 'kashafbucket-10nov2025'     # The name of the S3 bucket (from Line 7)
        }
        
        # 4. Write the item to the table
        table.put_item(Item=item_data)
        
        # --- DYNAMODB WRITE INSTRUCTIONS END HERE ---

        # upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=file_content,
            ContentType="image/jpeg"
        )

        # success response
        return {
            "statusCode":200,
            "headers":{"Content-Type": "application/json"},
            "body":json.dumps({"message": f"File uploaded successfully as {file_name}"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers":{"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})}