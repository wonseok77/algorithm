# Design Browser History
# 인터넷 브라우저에서 방문기록과 동일한 작동을 하는 BrowserHistory class를 구현할 것이다. 구현할 브라우저는 homepage에서 시작하고,
# 이후에는 다른 url에 방문할 수 있다. 또, "뒤로가기"와 "앞으로 가기"가 작동하도록 구현하라.


# - BrowserHistory(string homepage)를 호출하면 브라우저는 homepage에서 시작이 된다
# - void visit(string url)을 호출하면 현재 page의 앞에 있는 페이지기록은 다 삭제가 되고 url로 방문을 한다..
# - string back(int steps)을 호출하면 steps수 만큼 "뒤로 가기"를 한다. "뒤로 가기"를 할 수 있는 page 개수가 x 이고 step > x라면
#  x 번 만큼만 "뒤로 가기"를 한다. "뒤로 가기"가 완료되면 현재 url을 return한다.
# - string forward(int steps)을 호출하면 step수 만큼 "앞으로 가기"를 한다. "앞으로 가기"를 할 수 있는 page 개수가 x 이고 step > x라면
# x번 만큼만 "앞으로 가기"를 한다. "앞으로 가기"가 완료되면 현재 url을 return 한다.
# 


# 제약조건
# 1 <= homepage.length <= 20
# 1 <= url.length <= 20
# 1 <= step <= 100
# homepage와 url은 '.'를 포함한 lower case 영어 문자로 구성되어 있다.
# visit, back 그리고 forward는 최대 5000번의 호출이 있을 수 있다.

class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage str
        """
        
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """


### input
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("Linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)

### output
# None
# None
# None
# None
# "facebook.com"
# "google.com"
# "facebook.com"
# None
# "linkedin.com"
# "google.com"
# "leetcode.com"
