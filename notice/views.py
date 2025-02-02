from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice


# 공지사항 페이지 이동 뷰
class NoticeWebView(View):
    def get(self, request):
        return render(request, 'notice/web/notice.html')


class NoticeListAPI(APIView):
    # API에서 공지사항 목록을 가져오는 뷰
    # manager-notice.js에서 fetch로 요청받을 때 이 뷰가 사용된다
    def get(self, request, page):
        # 한 페이지 당 공지사항 최대 10개씩 표시
        row_count = 10

        # 한 페이지에 표시할 공지사항들을 슬라이싱 하기 위한 변수들
        offset = (page - 1) * row_count
        limit = page * row_count

        # 공지사항 표시에 필요한 tbl_notice의 컬럼들
        columns = [
            'id',
            'notice_title',
            'notice_content'
        ]

        # 게시 중인 공지사항의 제목과 내용을 10개씩 가져와서 notices에 할당(list)
        notices = Notice.enabled_objects.values(*columns)[offset:limit]

        # 다음 페이지에 표시할 공지사항이 있는지 판단하기 위한 변수
        # js로 페이지네이션을 구현하기 위함
        has_next_page = Notice.enabled_objects.filter()[limit:limit + 1].exists()

        # manager-notice.js에 보낼 공지사항 목록
        notice_info = {
            'notices': notices,
            'hasNext': has_next_page
        }

        # 요청한 목록 반환
        return Response(notice_info)