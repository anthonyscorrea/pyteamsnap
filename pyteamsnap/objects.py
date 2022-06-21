import apiclient.exceptions
from apiclient import APIClient, HeaderAuthentication, JsonResponseHandler, JsonRequestFormatter


class ApiObject():
    rel = None
    version = None
    template = None

    def __init__(self, client, rel=rel, data={}):
        self.client = client
        self.data = data
        self.rel = rel

    @classmethod
    def search(cls, client, **kwargs):
        try:
            results = client.query(cls.rel, "search", **kwargs)
        except apiclient.exceptions.ServerError as e:
            raise e
        return [cls(client,rel=cls.rel, data=r) for r in results]

    @classmethod
    def get(cls, client, id):
        r = client.get(f"{client.link(cls.rel)}/{id}")
        return cls(client, cls.rel, client.parse_response(r)[0])

    @classmethod
    def new(cls, client):
        return cls(client, cls.rel)

    def post(self):
        data = {
            "template":{
                "data": [{
                    "name":k,
                    "value":v
                } for k,v in self.data.items()]
            }
        }
        r = self.client.post_item(self.rel, data=data)
        self.data = r
        return r

    def put(self):
        data = {
            "template":{
                "data": [{
                    "name":k,
                    "value":str(v)
                } for k,v in self.data.items()]
            }
        }
        id = self.data.get('id')
        r = self.client.put_item(self.rel, id=id, data=data)
        self.data = r
        return r

    def delete(self):
        self.client.delete_item(self.rel, id=self.data['id'])

class Me (ApiObject):
    rel = "me"
    type = "user"
    version = "3.866.0"
    template = {
            "data": [
                {
                    "name": "first_name"
                },
                {
                    "name": "last_name"
                },
                {
                    "name": "password"
                },
                {
                    "name": "birthday"
                },
                {
                    "name": "email"
                },
                {
                    "name": "facebook_id",
                    "deprecated": True,
                    "prompt": "facebook_id is deprecated and has been removed.  Continued use of facebook_id is not recommended it will no longer be stored."
                },
                {
                    "name": "facebook_access_token",
                    "deprecated": True,
                    "prompt": "facebook_access_token is deprecated and has been removed.  Continued use of facebook_access_token is not recommended it will no longer be stored."
                },
                {
                    "name": "type",
                    "value": "user"
                },
                {
                    "name": "is_lab_rat"
                },
                {
                    "name": "receives_newsletter"
                }
            ]
        }

    def __init__(self, client):
        data = client.parse_response(client.get(client.link(self.rel)))[0]
        super().__init__(client=client, rel=self.rel, data=data)


class User (ApiObject):
    rel = "users"
    type = "user"
    version = "3.866.0"
    template = {
            "data": [
                {
                    "name": "first_name"
                },
                {
                    "name": "last_name"
                },
                {
                    "name": "password"
                },
                {
                    "name": "birthday"
                },
                {
                    "name": "email"
                },
                {
                    "name": "facebook_id",
                    "deprecated": True,
                    "prompt": "facebook_id is deprecated and has been removed.  Continued use of facebook_id is not recommended it will no longer be stored."
                },
                {
                    "name": "facebook_access_token",
                    "deprecated": True,
                    "prompt": "facebook_access_token is deprecated and has been removed.  Continued use of facebook_access_token is not recommended it will no longer be stored."
                },
                {
                    "name": "type",
                    "value": "user"
                },
                {
                    "name": "is_lab_rat"
                },
                {
                    "name": "receives_newsletter"
                }
            ]
        }

class Event (ApiObject):
    rel = "events"
    type = "event"
    version = "3.866.0"
    template = {
        "data": [
            {
                "name": "type",
                "value": "event"
            },
            {
                "name": "additional_location_details"
            },
            {
                "name": "browser_time_zone"
            },
            {
                "name": "division_location_id"
            },
            {
                "name": "doesnt_count_towards_record"
            },
            {
                "name": "duration_in_minutes"
            },
            {
                "name": "game_type_code"
            },
            {
                "name": "icon_color"
            },
            {
                "name": "is_canceled"
            },
            {
                "name": "is_game"
            },
            {
                "name": "is_overtime"
            },
            {
                "name": "is_shootout"
            },
            {
                "name": "is_tbd"
            },
            {
                "name": "label"
            },
            {
                "name": "location_id"
            },
            {
                "name": "minutes_to_arrive_early"
            },
            {
                "name": "name"
            },
            {
                "name": "notes"
            },
            {
                "name": "notify_opponent"
            },
            {
                "name": "notify_opponent_contacts_email"
            },
            {
                "name": "notify_opponent_contacts_name"
            },
            {
                "name": "notify_opponent_notes"
            },
            {
                "name": "notify_team"
            },
            {
                "name": "notify_team_as_member_id"
            },
            {
                "name": "opponent_id"
            },
            {
                "name": "points_for_opponent"
            },
            {
                "name": "points_for_team"
            },
            {
                "name": "repeating_include",
                "prompt": "When updating a repeating event, this is a required field. Values are: \"all\" - updates all events in this series, \"future\" - updates this event and all that occur after, \"none\" - only updates a single event."
            },
            {
                "name": "repeating_type_code",
                "prompt": "A app for the frequency of the repeated event, this is required with the \"repeating_include\" attribute when creating a repeating event. Valid values are: \"1\" - repeat an event daily, \"2\" - repeat an event weekly."
            },
            {
                "name": "repeating_until",
                "prompt": "A date when the repeating event should end, this is inclusive so an event will be created on this day if it falls before the next event specified by \"repeating_type_code\". This attribute is required with \"repeating_type_code\" when creating a repeating event."
            },
            {
                "name": "results"
            },
            {
                "name": "results_url"
            },
            {
                "name": "shootout_points_for_opponent"
            },
            {
                "name": "shootout_points_for_team"
            },
            {
                "name": "start_date"
            },
            {
                "name": "team_id"
            },
            {
                "name": "time_zone"
            },
            {
                "name": "tracks_availability"
            },
            {
                "name": "uniform"
            }
        ]}

class Team (ApiObject):
    rel = "teams"
    type = "team"
    version = "3.866.0"
    template = {
        "data": [
            {
                "name": "name"
            },
            {
                "name": "location_country"
            },
            {
                "name": "location_postal_code"
            },
            {
                "name": "time_zone",
                "prompt": "The time_zone parameter is required when creating a team, but for changing a team's time_zone, use the update_time_zone command"
            },
            {
                "name": "sport_id"
            },
            {
                "name": "division_id"
            },
            {
                "name": "division_name"
            },
            {
                "name": "season_name"
            },
            {
                "name": "league_name"
            },
            {
                "name": "league_url"
            },
            {
                "name": "owner_first_name"
            },
            {
                "name": "owner_last_name"
            },
            {
                "name": "owner_email"
            },
            {
                "name": "is_ownership_pending"
            },
            {
                "name": "ad_unit_hero_id"
            },
            {
                "name": "ad_unit_hero_template_id"
            },
            {
                "name": "ad_unit_inline_id"
            },
            {
                "name": "type",
                "value": "team"
            }
        ]
    }

class Availability (ApiObject):
    rel = "availabilities"
    type = "availability"
    version = "3.866.0"
    template = {
                   "data": [
                       {
                           "name": "status_code"
                       },
                       {
                           "name": "notes"
                       },
                       {
                           "name": "event_id"
                       },
                       {
                           "name": "member_id"
                       },
                       {
                           "name": "notes_author_member_id"
                       },
                       {
                           "name": "source"
                       },
                       {
                           "name": "type",
                           "value": "availability"
                       }
                   ]
               }

class Member (ApiObject):
    rel = "members"
    type = "member"
    version = "3.866.0"
    template = {
        "data": [
            {
                "name": "first_name"
            },
            {
                "name": "last_name"
            },
            {
                "name": "gender"
            },
            {
                "name": "position"
            },
            {
                "name": "is_manager"
            },
            {
                "name": "birthday"
            },
            {
                "name": "hide_age",
                "deprecated": True,
                "prompt": "hide_age is deprecated and will be removed in a future version, use is_age_hidden instead."
            },
            {
                "name": "is_age_hidden"
            },
            {
                "name": "hide_address",
                "deprecated": True,
                "prompt": "hide_address is deprecated and will be removed in a future version, use is_address_hidden instead."
            },
            {
                "name": "is_address_hidden"
            },
            {
                "name": "is_non_player"
            },
            {
                "name": "address_street1"
            },
            {
                "name": "address_street2"
            },
            {
                "name": "address_city"
            },
            {
                "name": "address_state"
            },
            {
                "name": "address_zip"
            },
            {
                "name": "jersey_number"
            },
            {
                "name": "team_id"
            },
            {
                "name": "is_ownership_pending"
            },
            {
                "name": "source_action"
            },
            {
                "name": "type",
                "value": "member"
            }
        ]
    },

class Location (ApiObject):
    rel = "locations"
    type = "location"
    version = "3.866.0"
    template = {
        "data": [
            {
                "name": "name"
            },
            {
                "name": "url"
            },
            {
                "name": "phone"
            },
            {
                "name": "notes"
            },
            {
                "name": "address"
            },
            {
                "name": "latitude"
            },
            {
                "name": "longitude"
            },
            {
                "name": "team_id"
            },
            {
                "name": "is_retired"
            },
            {
                "name": "type",
                "value": "location"
            }
        ]
    }

class Opponent (ApiObject):
    rel = "opponents"
    type = "opponent"
    version = "3.866.0"
    template = {
        "data": [
            {
                "name": "name"
            },
            {
                "name": "contacts_name"
            },
            {
                "name": "contacts_phone"
            },
            {
                "name": "contacts_email"
            },
            {
                "name": "notes"
            },
            {
                "name": "team_id"
            },
            {
                "name": "type",
                "value": "opponent"
            }
        ]
    }

class EventLineupEntry (ApiObject):
    rel = "event_lineup_entries"
    type = "event_lineup_entry"
    version = "3.866.0"
    template = {
            "data": [
                {
                    "name": "event_lineup_id"
                },
                {
                    "name": "member_id"
                },
                {
                    "name": "sequence"
                },
                {
                    "name": "label"
                },
                {
                    "name": "type",
                    "value": "event_lineup_entry"
                }
            ]
        }

    @classmethod
    def search(cls, client, **kwargs):
        # For some reason the query listed for search at this endpoint is for EventLineup, not EventLineupEntry
        # this is a workaround
        r = client.get(f"{client.link(cls.rel)}/search", params=kwargs)
        results = client.parse_response(r)
        [cls(client, rel=cls.rel, data=r) for r in results]
        return [cls(client, rel=cls.rel, data=r) for r in results]

class EventLineup (ApiObject):
    rel = "event_lineups"
    type = "event_lineup"
    version = "3.866.0"
    template = {}

class AvailabilitySummary (ApiObject):
    rel = "availability_summaries"
    type = "availability_summary"
    version = "3.866.0"
    template = {}

class Statistics (ApiObject):
    rel = "statistics"
    type = "statistic"
    version = "3.866.0"
    template = {
            "data": [
                {
                    "name": "acronym"
                },
                {
                    "name": "always_display_decimals"
                },
                {
                    "name": "formula"
                },
                {
                    "name": "is_in_descending_order"
                },
                {
                    "name": "display_zero_totals"
                },
                {
                    "name": "is_percentage"
                },
                {
                    "name": "is_private"
                },
                {
                    "name": "is_team_statistic"
                },
                {
                    "name": "is_top_statistic"
                },
                {
                    "name": "name"
                },
                {
                    "name": "precision"
                },
                {
                    "name": "statistic_group_id"
                },
                {
                    "name": "team_id"
                },
                {
                    "name": "type",
                    "value": "statistic"
                }
            ]
        }

class MemberStatistics (ApiObject):
    rel = "member_statistics"
