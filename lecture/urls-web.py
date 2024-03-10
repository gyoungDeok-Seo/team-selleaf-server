from django.urls import path

from lecture.views import LectureView, LectureDetailOnlineView, LectureDetailOfflineView, LectureTotalView, \
    LectureUploadOnlineView, LectureUploadOfflineView, LectureUpdateOnlineView, LectureUpdateOfflineView

app_name = 'lecture'

urlpatterns = [
    path('main/', LectureView.as_view(), name='main'),
    path('detail/online/', LectureDetailOnlineView.as_view(), name='detail-online'),
    path('detail/offline/', LectureDetailOfflineView.as_view(), name='detail-offline'),
    path('total/', LectureTotalView.as_view(), name='total'),
    path('upload/online/', LectureUploadOnlineView.as_view(), name='upload-online'),
    path('upload/offline/', LectureUploadOfflineView.as_view(), name='upload-offline'),
    path('update/online/', LectureUpdateOnlineView.as_view(), name='update-online'),
    path('update/offline/', LectureUpdateOfflineView.as_view(), name='update-offline'),

]
