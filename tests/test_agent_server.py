import unittest

from agent_server import build_agent_prompt, build_branch_plan_payload, build_health_payload


class AgentServerTests(unittest.TestCase):
    def test_health_payload_reports_ready(self):
        payload = build_health_payload()
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["service"], "xinocks-agent")
        self.assertEqual(payload["build_mode"], "deep")
        self.assertIn("timestamp", payload)

    def test_branch_plan_payload_exposes_adaptation_abilities(self):
        payload = build_branch_plan_payload()
        self.assertEqual(payload["concept"], "market-and-future-plan-variations")
        self.assertIn("adaptation_abilities", payload)
        self.assertIn("market_pressure_flow_scale", payload)
        self.assertIn("adaptive", payload["market_pressure_flow_scale"]["mode"])
        self.assertIn("user_choice_concept", payload)
        self.assertIn("guided", payload["user_choice_concept"]["default"])
        self.assertIn("user_choice_mode_for_all_choices", payload)
        self.assertIn("guided", payload["user_choice_mode_for_all_choices"]["default"])
        self.assertIn("fire_base_build_point", payload)
        self.assertTrue(payload["fire_base_build_point"]["for_user_desires"])
        self.assertIn("user_mode", payload)
        self.assertIn("guided", payload["user_mode"]["default"])
        self.assertIn("super_end_to_end_response", payload)
        self.assertIn("reasoning", payload["super_end_to_end_response"]["features"])
        self.assertIn("agi_build_feature", payload)
        self.assertEqual(payload["agi_build_feature"]["feature_grade"], "advanced")
        self.assertIn("tokenization_response", payload)
        self.assertTrue(payload["tokenization_response"]["when_needed"])

    def test_agent_prompt_includes_the_requested_behaviour(self):
        prompt = build_agent_prompt()
        self.assertIn("market pressure", prompt.lower())
        self.assertIn("guided", prompt.lower())
        self.assertIn("reasoning", prompt.lower())
        self.assertIn("task management", prompt.lower())


if __name__ == "__main__":
    unittest.main()
