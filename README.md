Admin Panel 
Username : milan
Password : 1


JWT login
login url : '/api/login/'
method : POST
body : {"username":"xxxxxxx", "password":"xxxxxxxx"}

Response:
{
    "access_token":"xxxxxxxxxxxxx",
    "refresh_token":"xxxxxxxxxxxxxxxx"
}


1. Questuion : What are the questions asked by me?
Api url : '/api/miniqa/question_list/'
method : GET
Header : barrier_token : access_token

Sample Response:
{
    "question_list": [
        {
            "id": "8142b6b3-e4d8-40f1-bd8e-34f98586ab60",
            "question_text": "What is the Best Backend Web Framework?",
            "date": "2020-07-13T18:21:23.199885Z"
        },
        {
            "id": "68e0d0b5-e1e0-4d3d-b0b9-f51a46001e4b",
            "question_text": "What is the Best source for leaning django?",
            "date": "2020-07-13T18:32:17.653984Z"
        }
    ]
}

2.Question : What are the answers given by me?
Api url : '/api/miniqa/answer_list/'
method : GET
Header : barrier_token : access_token

Sample Response:
{
    "answer_list": [
        {
            "id": "77d73d83-655d-45ec-b97f-78f131de1c31",
            "answer_text": "Django is The best Backend web framework",
            "date": "2020-07-13T18:36:46.551827Z"
        },
        {
            "id": "35f636e7-9453-461e-ae5b-f32dec099d30",
            "answer_text": "Django Documentation is the best source for learning django",
            "date": "2020-07-13T18:43:28.848933Z"
        }
    ]
}

3.Question : What are the upvotes done by me?
Api url : '/api/miniqa/upvote_list/'
method : GET
Header : barrier_token : access_token

Sample Response:
{
    "upvote_list": [
        {
            "id": "f2493e21-fc0f-4fdc-b736-9e97eab2444b",
            "answer__answer_text": "Django is The best Backend web framework",
            "date": "2020-07-13T18:45:46.931448Z"
        },
        {
            "id": "c9b3eb6e-9372-4ceb-a8de-7503efcbfc27",
            "answer__answer_text": "Laravel is the best web framework",
            "date": "2020-07-13T18:45:54.293495Z"
        }
    ]
}

4.Question : What are the answers to a given question?
Api url : "/api/miniqa/question/8142b6b3-e4d8-40f1-bd8e-34f98586ab60/answer_list/"
paramiter : question id
method : GET

sample response:
{
    "question": "What is the Best Backend Web Framework?",
    "answer_list": [
        {
            "answer_text": "Django is The best Backend web framework"
        },
        {
            "answer_text": "Laravel is the best web framework"
        }
    ]
}

5.Who has all upvoted a given question’s answer?
Api Url : "/api/miniqa/answer/35f636e7-9453-461e-ae5b-f32dec099d30/upvoted_list/"
paramiter : answer id
method : "GET"

Sample Response
{
    "question": "What is the Best source for leaning django?",
    "answer": "Django Documentation is the best source for learning django",
    "upvoted_by": [
        {
            "upvoted_by__username": "milan"
        },
        {
            "upvoted_by__username": "sumit"
        }
    ]
}

6.Across the entire application, which question has had the highest number of upvotes over the past hour.
Api url: "/api/miniqa/question/highest_upvote/last_hour/"
method : "GET"

Sample Response:
{
    "question": "What is the Best Backend Web Framework?",
    "max_upvote": 1
}

7. Across the entire application, which question has had the highest number of votes ever.
Api url : "/api/miniqa/question/highest_upvote/"
method : "GET"

Sample Request:
{
    "question": "What is the Best Backend Web Framework?",
    "max_upvote": 4
}
