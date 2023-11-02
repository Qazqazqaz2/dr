import requests

headers = {
            "content-type": "application/json; charset=utf-8",
            "Host": "www.instagram.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.instagram.com/jessaclan/followers/",
            "X-CSRFToken": "U8n4wP1ejItzTkUIKwWGv5q5E9CcBTqc",
            "X-IG-App-ID": "936619743392459",
            "X-ASBD-ID": "129477",
            "X-IG-WWW-Claim": "hmac.AR3npCQEim7gEfMiY23HIlZKhpuHEuNzGWwGjZa_6unduC5O",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Cookie": 'csrftoken=U8n4wP1ejItzTkUIKwWGv5q5E9CcBTqc; mid=ZUJUCQALAAFIFf5MVEdpwFQ2_gXG; ig_did=26213F82-53DC-4CB5-B08D-98A76E78D663; dpr=2; datr=MVRCZYfB5mVCL2dBL_iSnTiu; rur="LLA\05446687667085\0541730382317:01f798d7717391ab1166b1a1324b4f662d8ee703c73e07eabaa2884ad543c727b4a491e8"; ds_user_id=46687667085; sessionid=46687667085%3AyCBLAUTtskBOv7%3A24%3AAYdZ2GcsbWDviqKQLYQC3tm9X7M4pOX6tn1pftFdZQ',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
          }

print(requests.get('https://www.instagram.com/api/v1/friendships/61233172589/followers/?count=12&max_id=48&search_surface=follow_list_page', headers=headers).json())
