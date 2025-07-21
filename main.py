from email_client import EmailClient
from message_processor import MessageProcessor
from responder import Responder
from action_manager import ActionManager
from pprint import pprint as pp


def main():
    # init modules
    email_client = EmailClient()
    processor = MessageProcessor()
    responder = Responder()
    action_mgr = ActionManager()

    # process and respond to recent unread
    messages = email_client.fetch_unread_messages()
    for msg in messages:
        parsed_email = processor.parse_email(msg)
        reply_raw = responder.generate_reply(parsed_email)
        reply, action_data = responder.clean_reply(reply_raw)
        unit, actions = responder.parse_unit_and_actions(action_data)

        pp(f"\nReply:\n{reply}\n")
        pp(f"Action Items for Unit {unit}:\n{actions}\n")

        # send email response
        email_client.send_reply(parsed_email, reply)
        # saves action items to file
        action_mgr.process_and_save(parsed_email, unit, actions)

if __name__ == "__main__":
    main()
