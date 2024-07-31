# Created by Kaitlin Purdham
# last updated 7/31/2024

import base64
import json
import requests
import csv


# Function Definitions
def set_group_id(organization):
    # assign values based on request input
    ticket_group_id = ""

    if organization == "Pod 1":
        ticket_group_id = 26493689574939
    elif organization == "Pod 2":
        ticket_group_id = 26493681178779
    elif organization == "Pod 3":
        ticket_group_id = 26493710060827
    elif organization == "Pod 4":
        ticket_group_id = 26493681178779
    elif organization == "Pod 5":
        ticket_group_id = 26493725974555
    elif organization == "Pod 6":
        ticket_group_id = 26493695583003
    elif organization == "Pod 7":
        ticket_group_id = 26493726040731
    elif organization == "Pod 8":
        ticket_group_id = 26493681452955
    elif organization == "Pod 9":
        ticket_group_id = 26493695746971
    elif organization == "Pod 10":
        ticket_group_id = 26493690007707
    elif organization == "Pod 11":
        ticket_group_id = 26493681618843
    elif organization == "Pod 12":
        ticket_group_id = 26493690109979
    elif organization == "Pod 13":
        ticket_group_id = 26493710523035
    elif organization == "Pod 14":
        ticket_group_id = 26493726357019
    elif organization == "Pod 15":
        ticket_group_id = 26493710655387
    elif organization == "Pod 16":
        ticket_group_id = 26493726459419
    elif organization == "Pod 17":
        ticket_group_id = 26493740757531
    else:
        ticket_group_id = "-"

    return ticket_group_id


# def set_brand_id(group_text):


if __name__ == "__main__":
    # gather input, assign values
    input_ticket_id = "851"

    # zendesk auth parameters
    input_email = "email@email.com"
    input_zendesk_api_token = "<api_token>"
    input_domain = "<zendesk_domain_name>"
    # Base64 encode authentication
    auth = base64.b64encode(
        bytes(f"{input_email}/token:{input_zendesk_api_token}", "utf-8")
    ).decode("ascii")

    # Set the headers and url for the api requests
    headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}
    url = f"https://{input_domain}.zendesk.com/api/v2/tickets/{input_ticket_id}"

    # GET request for ticket
    ticket = requests.get(url, headers=headers)

    if ticket.status_code == 200:

        # get the json of ticket
        ticket_json = ticket.json()

        # define ticket fields from the full ticket json for future use
        ticket_url = ticket_json["ticket"]["url"]
        ticket_external_id = ticket_json["ticket"]["external_id"]

        ticket_via = ticket_json["ticket"]["via"]
        ticket_via_channel = ticket_via["channel"]
        ticket_via_source = ticket_via["source"]
        ticket_via_source_from = ticket_via["source"]["from"]
        ticket_via_source_to = ticket_via["source"]["to"]
        ticket_via_source_rel = ticket_via["source"]["rel"]

        ticket_created_at = ticket_json["ticket"]["created_at"]
        ticket_updated_at = ticket_json["ticket"]["updated_at"]
        ticket_generated_timestamp = ticket_json["ticket"]["generated_timestamp"]
        ticket_type = ticket_json["ticket"]["type"]
        ticket_subject = ticket_json["ticket"]["subject"]
        ticket_raw_subject = ticket_json["ticket"]["raw_subject"]
        ticket_description = ticket_json["ticket"]["description"]
        ticket_priority = ticket_json["ticket"]["priority"]
        ticket_status = ticket_json["ticket"]["status"]
        ticket_recipient = ticket_json["ticket"]["recipient"]
        ticket_requestor_id = ticket_json["ticket"]["requestor_id"]
        ticket_submitter_id = ticket_json["ticket"]["submitter_id"]
        ticket_assignee_id = ticket_json["ticket"]["assignee_id"]
        ticket_organization_id = ticket_json["ticket"]["organization_id"]
        ticket_group_id = ticket_json["ticket"]["group_id"]
        ticket_collaborator_ids = ticket_json["ticket"]["collaborator_ids"]
        ticket_follower_ids = ticket_json["ticket"]["follower_ids"]
        ticket_email_cc_ids = ticket_json["ticket"]["email_cc_ids"]
        ticket_forum_topic_id = ticket_json["ticket"]["forum_topic_id"]
        ticket_problem_id = ticket_json["ticket"]["problem_id"]
        ticket_has_incidents = ticket_json["ticket"]["has_incidents"]
        ticket_is_public = ticket_json["ticket"]["is_public"]
        ticket_due_at = ticket_json["ticket"]["due_at"]
        ticket_tags_array = ticket_json["ticket"]["tags"]
        ticket_custom_fields_array = ticket_json["ticket"]["custom_fields"]
        ticket_satisfaction_rating = ticket_json["ticket"]["satisfaction_rating"]
        ticket_sharing_agreement_ids_array = ticket_json["ticket"][
            "sharing_agreement_ids"
        ]
        ticket_custom_status_id = ticket_json["ticket"]["custom_status_id"]
        ticket_fields_array = ticket_json["ticket"]["fields"]

        # prepare updated json
        # updated_ticket_json = {
        #   "ticket": {
        #      "group_id": ticket_json["ticket"]["group_id"]
        #       }
        # }

        # send PUT request to update the ticket
        # response = requests.put(url, headers=headers, json=updated_ticket_json)

        # Check if update was successful
        if response.status_code == 200:
            print("Ticket updated successfully.")
        else:
            print(f"Failed to update ticket. Status code: {response.status_code}")
