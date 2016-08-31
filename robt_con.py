def sc():
    from slackclient import SlackClient
    import websocket
    import json
   


    token = "your slack taken"
    sc = SlackClient(token)
    print(sc.api_call("api.test"))
    print(sc.api_call("channels.info", channel="1234567890"))
    print(sc.api_call(
            "chat.postMessage", channel="#your slack channel", text="I do it.Message from python",
            username='robt_01', icon_emoji=':robot_face:'
    )
    )




