import config
import kasa


if __name__ == '__main__':
    payload_from_iot = {
        "batteryVoltage": "1555mV",
        "serialNumber": config.IOT_BUTTON_SERIAL_NUMBER,
        "clickType": "SINGLE"  # or "DOUBLE" or "LONG"
    }
    kasa.lambda_handler(payload_from_iot, None)
