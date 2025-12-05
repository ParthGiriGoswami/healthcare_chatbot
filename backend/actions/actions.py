from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCheckSufficientFunds(Action):
    def name(self) -> Text:
        return "action_check_sufficient_funds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # hard-coded balance for tutorial purposes.
        # This value is now also set as a slot.
        balance = 1000.0 # Using float for consistency
        transfer_amount = tracker.get_slot("amount")
        
        has_sufficient_funds = transfer_amount <= balance
        
        # Set both slots: the balance value and the check result
        return [
            SlotSet("current_balance", balance), # <-- Sets the current balance
            SlotSet("has_sufficient_funds", has_sufficient_funds)
        ]