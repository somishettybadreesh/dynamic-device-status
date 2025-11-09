# blueprints/api.py
from flask import Blueprint, jsonify, request
from services.device_service import get_companies, get_devices_with_status

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/companies', methods=['GET'])
def companies():
    try:
        rows = get_companies()
        return jsonify({"success": True, "companies": rows}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@api.route('/companies/<int:company_id>/devices', methods=['GET'])
def devices(company_id):
    try:
        devices = get_devices_with_status(company_id)
        return jsonify({"success": True, "devices": devices}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
