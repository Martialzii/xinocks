import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = os.getenv("AGENT_HOST", "127.0.0.1")
PORT = int(os.getenv("AGENT_PORT", "8010"))
SERVICE_NAME = "xinocks-agent"
BUILD_MODE = os.getenv("BUILD_MODE", "deep")


def build_health_payload():
    return {
        "status": "ok",
        "service": SERVICE_NAME,
        "build_mode": BUILD_MODE,
        "languages": [
            {"name": "Python", "category": "runtime"},
            {"name": "Django", "category": "framework"},
            {"name": "Azure", "category": "cloud"},
            {"name": "HTML/CSS/JS", "category": "frontend"},
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def build_branch_plan_payload():
    return {
        "concept": "market-and-future-plan-variations",
        "sources": ["market", "future-plans", "experimental"],
        "status": "ready",
        "adaptation_abilities": [
            "market_pressure_response",
            "flow_scaling",
            "adaptive_rebalance"
        ],
        "user_choice_concept": {
            "mode": "selectable",
            "options": ["auto", "manual", "guided"],
            "default": "guided"
        },
        "user_choice_mode_for_all_choices": {
            "mode": "selectable",
            "applies_to": ["adaptation", "tokenization", "flow_scale", "response_style"],
            "default": "guided"
        },
        "fire_base_build_point": {
            "mode": "printable",
            "for_user_desires": True,
            "output_style": "clear_summary"
        },
        "user_mode": {
            "mode": "selectable",
            "options": ["standard", "adaptive", "guided"],
            "default": "guided"
        },
        "super_end_to_end_response": {
            "mode": "resilient",
            "features": [
                "response_resistant",
                "task_management",
                "reasoning"
            ],
            "default": "guided"
        },
        "agi_build_feature": {
            "mode": "max_potential",
            "feature_grade": "advanced",
            "focus": ["scaling", "reasoning", "adaptation"]
        },
        "tokenization_response": {
            "mode": "optional",
            "when_needed": True,
            "format": "structured_tokens"
        },
        "market_pressure_flow_scale": {
            "mode": "adaptive",
            "levels": ["low", "medium", "high", "critical"],
            "default": "medium"
        },
    }


class AgentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in {"/", "/health", "/healthz"}:
            self._send_json(200, build_health_payload())
            return
        if self.path == "/info":
            self._send_json(200, {
                "service": SERVICE_NAME,
                "message": "Xinocks agent server ready for Foundry Toolkit Agent Inspector",
                "build_mode": BUILD_MODE,
                "features": ["health", "info", "build", "message"],
                "languages": [
                    {"name": "Python", "category": "runtime"},
                    {"name": "Django", "category": "framework"},
                    {"name": "Azure", "category": "cloud"},
                    {"name": "HTML/CSS/JS", "category": "frontend"},
                ],
            })
            return
        if self.path == "/build":
            self._send_json(200, {
                "service": SERVICE_NAME,
                "build_mode": BUILD_MODE,
                "status": "ready",
                "checks": ["server", "health_endpoint", "debug_profile"],
                "languages": [
                    {"name": "Python", "category": "runtime"},
                    {"name": "Django", "category": "framework"},
                    {"name": "Azure", "category": "cloud"},
                    {"name": "HTML/CSS/JS", "category": "frontend"},
                ],
                "branch_plan": build_branch_plan_payload(),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })
            return
        if self.path == "/plan-variants":
            self._send_json(200, build_branch_plan_payload())
            return
        self._send_json(404, {"error": "Not Found"})

    def do_POST(self):
        if self.path == "/message":
            content_length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(content_length).decode("utf-8") or "{}"
            try:
                payload = json.loads(body)
            except json.JSONDecodeError:
                payload = {"raw": body}
            self._send_json(200, {
                "status": "received",
                "service": SERVICE_NAME,
                "build_mode": BUILD_MODE,
                "payload": payload,
            })
            return
        self._send_json(404, {"error": "Not Found"})

    def _send_json(self, status_code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def main():
    server = ThreadingHTTPServer((HOST, PORT), AgentHandler)
    print(f"{SERVICE_NAME} listening on http://{HOST}:{PORT} in {BUILD_MODE} mode")
    server.serve_forever()


if __name__ == "__main__":
    main()
