from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.detector import detect_objects
from PIL import Image
import io

app = FastAPI(title="MedEdu Vision AI")

@app.get("/")
def health_check():
    return {"status": "MedEdu Vision AI running"}

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        results = detect_objects(image)

        return JSONResponse(
            content={
                "success": True,
                "detections": results
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "error": str(e)}
        )
