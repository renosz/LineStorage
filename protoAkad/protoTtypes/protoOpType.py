class OpType(object):
    END_OF_OPERATION = 0
    UPDATE_PROFILE = 1
    UPDATE_SETTINGS = 36
    NOTIFIED_UPDATE_PROFILE = 2
    REGISTER_USERID = 3
    ADD_CONTACT = 4
    NOTIFIED_ADD_CONTACT = 5
    BLOCK_CONTACT = 6
    UNBLOCK_CONTACT = 7
    NOTIFIED_RECOMMEND_CONTACT = 8
    CREATE_GROUP = 9
    UPDATE_GROUP = 10
    NOTIFIED_UPDATE_GROUP = 11
    INVITE_INTO_GROUP = 12
    NOTIFIED_INVITE_INTO_GROUP = 13
    CANCEL_INVITATION_GROUP = 31
    NOTIFIED_CANCEL_INVITATION_GROUP = 32
    LEAVE_GROUP = 14
    NOTIFIED_LEAVE_GROUP = 15
    ACCEPT_GROUP_INVITATION = 16
    NOTIFIED_ACCEPT_GROUP_INVITATION = 17
    REJECT_GROUP_INVITATION = 34
    NOTIFIED_REJECT_GROUP_INVITATION = 35
    KICKOUT_FROM_GROUP = 18
    NOTIFIED_KICKOUT_FROM_GROUP = 19
    CREATE_ROOM = 20
    INVITE_INTO_ROOM = 21
    NOTIFIED_INVITE_INTO_ROOM = 22
    LEAVE_ROOM = 23
    NOTIFIED_LEAVE_ROOM = 24
    SEND_MESSAGE = 25
    RECEIVE_MESSAGE = 26
    SEND_NOTIFIED_READ_MESSAGECEIPT = 27
    RECEIVE_MESSAGE_RECEIPT = 28
    SEND_CONTENT_RECEIPT = 29
    RECEIVE_ANNOUNCEMENT = 30
    NOTIFIED_UNREGISTER_USER = 33
    INVITE_VIA_EMAIL = 38
    NOTIFIED_REGISTER_USER = 37
    NOTIFIED_REQUEST_RECOVERY = 39
    SEND_CHAT_CHECKED = 40
    SEND_CHAT_REMOVED = 41
    NOTIFIED_FORCE_SYNC = 42
    SEND_CONTENT = 43
    SEND_MESSAGE_MYHOME = 44
    NOTIFIED_UPDATE_CONTENT_PREVIEW = 45
    REMOVE_ALL_MESSAGES = 46
    NOTIFIED_UPDATE_PURCHASES = 47
    DUMMY = 48
    UPDATE_CONTACT = 49
    NOTIFIED_RECEIVED_CALL = 50
    CANCEL_CALL = 51
    NOTIFIED_REDIRECT = 52
    NOTIFIED_CHANNEL_SYNC = 53
    FAILED_SEND_MESSAGE = 54
    NOTIFIED_READ_MESSAGE = 55
    FAILED_EMAIL_CONFIRMATION = 56
    NOTIFIED_CHAT_CONTENT = 58
    NOTIFIED_PUSH_NOTICENTER_ITEM = 59
    NOTIFIED_JOIN_CHAT = 60
    NOTIFIED_LEAVE_CHAT = 61
    NOTIFIED_TYPING = 62
    FRIEND_REQUEST_ACCEPTED = 63
    DESTROY_MESSAGE = 64
    NOTIFIED_DESTROY_MESSAGE = 65
    UPDATE_PUBLICKEYCHAIN = 66
    NOTIFIED_UPDATE_PUBLICKEYCHAIN = 67
    NOTIFIED_BLOCK_CONTACT = 68
    NOTIFIED_UNBLOCK_CONTACT = 69
    UPDATE_GROUPPREFERENCE = 70
    NOTIFIED_PAYMENT_EVENT = 71
    REGISTER_E2EE_PUBLICKEY = 72
    NOTIFIED_E2EE_KEY_EXCHANGE_REQ = 73
    NOTIFIED_E2EE_KEY_EXCHANGE_RESP = 74
    NOTIFIED_E2EE_MESSAGE_RESEND_REQ = 75
    NOTIFIED_E2EE_MESSAGE_RESEND_RESP = 76
    NOTIFIED_E2EE_KEY_UPDATE = 77
    NOTIFIED_BUDDY_UPDATE_PROFILE = 78
    NOTIFIED_UPDATE_LINEAT_TABS = 79
    UPDATE_ROOM = 80
    NOTIFIED_BEACON_DETECTED = 81
    UPDATE_EXTENDED_PROFILE = 82
    ADD_FOLLOW = 83
    NOTIFIED_ADD_FOLLOW = 84
    DELETE_FOLLOW = 85
    NOTIFIED_DELETE_FOLLOW = 86
    UPDATE_TIMELINE_SETTINGS = 87
    NOTIFIED_FRIEND_REQUEST = 88
    UPDATE_RINGBACK_TONE = 89
    NOTIFIED_POSTBACK = 90
    RECEIVE_READ_WATERMARK = 91
    NOTIFIED_MESSAGE_DELIVERED = 92
    NOTIFIED_UPDATE_CHAT_BAR = 93
    NOTIFIED_CHATAPP_INSTALLED = 94
    NOTIFIED_CHATAPP_UPDATED = 95
    NOTIFIED_CHATAPP_NEW_MARK = 96
    NOTIFIED_CHATAPP_DELETED = 97
    NOTIFIED_CHATAPP_SYNC = 98
    NOTIFIED_UPDATE_MESSAGE = 99

    _VALUES_TO_NAMES = {
        0: "END_OF_OPERATION",
        1: "UPDATE_PROFILE",
        36: "UPDATE_SETTINGS",
        2: "NOTIFIED_UPDATE_PROFILE",
        3: "REGISTER_USERID",
        4: "ADD_CONTACT",
        5: "NOTIFIED_ADD_CONTACT",
        6: "BLOCK_CONTACT",
        7: "UNBLOCK_CONTACT",
        8: "NOTIFIED_RECOMMEND_CONTACT",
        9: "CREATE_GROUP",
        10: "UPDATE_GROUP",
        11: "NOTIFIED_UPDATE_GROUP",
        12: "INVITE_INTO_GROUP",
        13: "NOTIFIED_INVITE_INTO_GROUP",
        31: "CANCEL_INVITATION_GROUP",
        32: "NOTIFIED_CANCEL_INVITATION_GROUP",
        14: "LEAVE_GROUP",
        15: "NOTIFIED_LEAVE_GROUP",
        16: "ACCEPT_GROUP_INVITATION",
        17: "NOTIFIED_ACCEPT_GROUP_INVITATION",
        34: "REJECT_GROUP_INVITATION",
        35: "NOTIFIED_REJECT_GROUP_INVITATION",
        18: "KICKOUT_FROM_GROUP",
        19: "NOTIFIED_KICKOUT_FROM_GROUP",
        20: "CREATE_ROOM",
        21: "INVITE_INTO_ROOM",
        22: "NOTIFIED_INVITE_INTO_ROOM",
        23: "LEAVE_ROOM",
        24: "NOTIFIED_LEAVE_ROOM",
        25: "SEND_MESSAGE",
        26: "RECEIVE_MESSAGE",
        27: "SEND_MESSAGE_RECEIPT",
        28: "RECEIVE_MESSAGE_RECEIPT",
        29: "SEND_CONTENT_RECEIPT",
        30: "RECEIVE_ANNOUNCEMENT",
        33: "NOTIFIED_UNREGISTER_USER",
        38: "INVITE_VIA_EMAIL",
        37: "NOTIFIED_REGISTER_USER",
        39: "NOTIFIED_REQUEST_RECOVERY",
        40: "SEND_CHAT_CHECKED",
        41: "SEND_CHAT_REMOVED",
        42: "NOTIFIED_FORCE_SYNC",
        43: "SEND_CONTENT",
        44: "SEND_MESSAGE_MYHOME",
        45: "NOTIFIED_UPDATE_CONTENT_PREVIEW",
        46: "REMOVE_ALL_MESSAGES",
        47: "NOTIFIED_UPDATE_PURCHASES",
        48: "DUMMY",
        49: "UPDATE_CONTACT",
        50: "NOTIFIED_RECEIVED_CALL",
        51: "CANCEL_CALL",
        52: "NOTIFIED_REDIRECT",
        53: "NOTIFIED_CHANNEL_SYNC",
        54: "FAILED_SEND_MESSAGE",
        55: "NOTIFIED_READ_MESSAGE",
        56: "FAILED_EMAIL_CONFIRMATION",
        58: "NOTIFIED_CHAT_CONTENT",
        59: "NOTIFIED_PUSH_NOTICENTER_ITEM",
        60: "NOTIFIED_JOIN_CHAT",
        61: "NOTIFIED_LEAVE_CHAT",
        62: "NOTIFIED_TYPING",
        63: "FRIEND_REQUEST_ACCEPTED",
        64: "DESTROY_MESSAGE",
        65: "NOTIFIED_DESTROY_MESSAGE",
        66: "UPDATE_PUBLICKEYCHAIN",
        67: "NOTIFIED_UPDATE_PUBLICKEYCHAIN",
        68: "NOTIFIED_BLOCK_CONTACT",
        69: "NOTIFIED_UNBLOCK_CONTACT",
        70: "UPDATE_GROUPPREFERENCE",
        71: "NOTIFIED_PAYMENT_EVENT",
        72: "REGISTER_E2EE_PUBLICKEY",
        73: "NOTIFIED_E2EE_KEY_EXCHANGE_REQ",
        74: "NOTIFIED_E2EE_KEY_EXCHANGE_RESP",
        75: "NOTIFIED_E2EE_MESSAGE_RESEND_REQ",
        76: "NOTIFIED_E2EE_MESSAGE_RESEND_RESP",
        77: "NOTIFIED_E2EE_KEY_UPDATE",
        78: "NOTIFIED_BUDDY_UPDATE_PROFILE",
        79: "NOTIFIED_UPDATE_LINEAT_TABS",
        80: "UPDATE_ROOM",
        81: "NOTIFIED_BEACON_DETECTED",
        82: "UPDATE_EXTENDED_PROFILE",
        83: "ADD_FOLLOW",
        84: "NOTIFIED_ADD_FOLLOW",
        85: "DELETE_FOLLOW",
        86: "NOTIFIED_DELETE_FOLLOW",
        87: "UPDATE_TIMELINE_SETTINGS",
        88: "NOTIFIED_FRIEND_REQUEST",
        89: "UPDATE_RINGBACK_TONE",
        90: "NOTIFIED_POSTBACK",
        91: "RECEIVE_READ_WATERMARK",
        92: "NOTIFIED_MESSAGE_DELIVERED",
        93: "NOTIFIED_UPDATE_CHAT_BAR",
        94: "NOTIFIED_CHATAPP_INSTALLED",
        95: "NOTIFIED_CHATAPP_UPDATED",
        96: "NOTIFIED_CHATAPP_NEW_MARK",
        97: "NOTIFIED_CHATAPP_DELETED",
        98: "NOTIFIED_CHATAPP_SYNC",
        99: "NOTIFIED_UPDATE_MESSAGE",
    }

    _NAMES_TO_VALUES = {
        "END_OF_OPERATION": 0,
        "UPDATE_PROFILE": 1,
        "UPDATE_SETTINGS": 36,
        "NOTIFIED_UPDATE_PROFILE": 2,
        "REGISTER_USERID": 3,
        "ADD_CONTACT": 4,
        "NOTIFIED_ADD_CONTACT": 5,
        "BLOCK_CONTACT": 6,
        "UNBLOCK_CONTACT": 7,
        "NOTIFIED_RECOMMEND_CONTACT": 8,
        "CREATE_GROUP": 9,
        "UPDATE_GROUP": 10,
        "NOTIFIED_UPDATE_GROUP": 11,
        "INVITE_INTO_GROUP": 12,
        "NOTIFIED_INVITE_INTO_GROUP": 13,
        "CANCEL_INVITATION_GROUP": 31,
        "NOTIFIED_CANCEL_INVITATION_GROUP": 32,
        "LEAVE_GROUP": 14,
        "NOTIFIED_LEAVE_GROUP": 15,
        "ACCEPT_GROUP_INVITATION": 16,
        "NOTIFIED_ACCEPT_GROUP_INVITATION": 17,
        "REJECT_GROUP_INVITATION": 34,
        "NOTIFIED_REJECT_GROUP_INVITATION": 35,
        "KICKOUT_FROM_GROUP": 18,
        "NOTIFIED_KICKOUT_FROM_GROUP": 19,
        "CREATE_ROOM": 20,
        "INVITE_INTO_ROOM": 21,
        "NOTIFIED_INVITE_INTO_ROOM": 22,
        "LEAVE_ROOM": 23,
        "NOTIFIED_LEAVE_ROOM": 24,
        "SEND_MESSAGE": 25,
        "RECEIVE_MESSAGE": 26,
        "SEND_MESSAGE_RECEIPT": 27,
        "RECEIVE_MESSAGE_RECEIPT": 28,
        "SEND_CONTENT_RECEIPT": 29,
        "RECEIVE_ANNOUNCEMENT": 30,
        "NOTIFIED_UNREGISTER_USER": 33,
        "INVITE_VIA_EMAIL": 38,
        "NOTIFIED_REGISTER_USER": 37,
        "NOTIFIED_REQUEST_RECOVERY": 39,
        "SEND_CHAT_CHECKED": 40,
        "SEND_CHAT_REMOVED": 41,
        "NOTIFIED_FORCE_SYNC": 42,
        "SEND_CONTENT": 43,
        "SEND_MESSAGE_MYHOME": 44,
        "NOTIFIED_UPDATE_CONTENT_PREVIEW": 45,
        "REMOVE_ALL_MESSAGES": 46,
        "NOTIFIED_UPDATE_PURCHASES": 47,
        "DUMMY": 48,
        "UPDATE_CONTACT": 49,
        "NOTIFIED_RECEIVED_CALL": 50,
        "CANCEL_CALL": 51,
        "NOTIFIED_REDIRECT": 52,
        "NOTIFIED_CHANNEL_SYNC": 53,
        "FAILED_SEND_MESSAGE": 54,
        "NOTIFIED_READ_MESSAGE": 55,
        "FAILED_EMAIL_CONFIRMATION": 56,
        "NOTIFIED_CHAT_CONTENT": 58,
        "NOTIFIED_PUSH_NOTICENTER_ITEM": 59,
        "NOTIFIED_JOIN_CHAT": 60,
        "NOTIFIED_LEAVE_CHAT": 61,
        "NOTIFIED_TYPING": 62,
        "FRIEND_REQUEST_ACCEPTED": 63,
        "DESTROY_MESSAGE": 64,
        "NOTIFIED_DESTROY_MESSAGE": 65,
        "UPDATE_PUBLICKEYCHAIN": 66,
        "NOTIFIED_UPDATE_PUBLICKEYCHAIN": 67,
        "NOTIFIED_BLOCK_CONTACT": 68,
        "NOTIFIED_UNBLOCK_CONTACT": 69,
        "UPDATE_GROUPPREFERENCE": 70,
        "NOTIFIED_PAYMENT_EVENT": 71,
        "REGISTER_E2EE_PUBLICKEY": 72,
        "NOTIFIED_E2EE_KEY_EXCHANGE_REQ": 73,
        "NOTIFIED_E2EE_KEY_EXCHANGE_RESP": 74,
        "NOTIFIED_E2EE_MESSAGE_RESEND_REQ": 75,
        "NOTIFIED_E2EE_MESSAGE_RESEND_RESP": 76,
        "NOTIFIED_E2EE_KEY_UPDATE": 77,
        "NOTIFIED_BUDDY_UPDATE_PROFILE": 78,
        "NOTIFIED_UPDATE_LINEAT_TABS": 79,
        "UPDATE_ROOM": 80,
        "NOTIFIED_BEACON_DETECTED": 81,
        "UPDATE_EXTENDED_PROFILE": 82,
        "ADD_FOLLOW": 83,
        "NOTIFIED_ADD_FOLLOW": 84,
        "DELETE_FOLLOW": 85,
        "NOTIFIED_DELETE_FOLLOW": 86,
        "UPDATE_TIMELINE_SETTINGS": 87,
        "NOTIFIED_FRIEND_REQUEST": 88,
        "UPDATE_RINGBACK_TONE": 89,
        "NOTIFIED_POSTBACK": 90,
        "RECEIVE_READ_WATERMARK": 91,
        "NOTIFIED_MESSAGE_DELIVERED": 92,
        "NOTIFIED_UPDATE_CHAT_BAR": 93,
        "NOTIFIED_CHATAPP_INSTALLED": 94,
        "NOTIFIED_CHATAPP_UPDATED": 95,
        "NOTIFIED_CHATAPP_NEW_MARK": 96,
        "NOTIFIED_CHATAPP_DELETED": 97,
        "NOTIFIED_CHATAPP_SYNC": 98,
        "NOTIFIED_UPDATE_MESSAGE": 99,
    }


class PayloadType(object):
    PAYLOAD_BUY = 101
    PAYLOAD_CS = 111
    PAYLOAD_BONUS = 121
    PAYLOAD_EVENT = 131

    _VALUES_TO_NAMES = {
        101: "PAYLOAD_BUY",
        111: "PAYLOAD_CS",
        121: "PAYLOAD_BONUS",
        131: "PAYLOAD_EVENT",
    }

    _NAMES_TO_VALUES = {
        "PAYLOAD_BUY": 101,
        "PAYLOAD_CS": 111,
        "PAYLOAD_BONUS": 121,
        "PAYLOAD_EVENT": 131,
    }