from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .models import FileModel
import uuid

def index(request):
  if request.COOKIES.get('id') == None:
    response = render(request,'top/index.html')
    str_uuid = str(uuid.uuid4())
    response.set_cookie(key='id',value=str_uuid)
  else:
    user_id = request.COOKIES.get('id')
    files = FileModel.objects.filter(user_id=user_id)
    params = {'files':files}
    response = render(request,'top/index.html',params)
  return response

def upload_file(request):
  obj = FileModel()
  if request.method == 'POST':
    #form = UploadFileForm(request.POST,request.FILES,instance=obj)
    if file_valid(request.FILES.get('file')):
      obj.user_id = request.POST.get('id')
      obj.src_file = request.FILES.get('file')
      obj.save()
      result_set = {'result':True,'msg':'アップロードが完了しました'}
    else:
      result_set = {'result':False,'msg':'不正なファイルです'}
    return JsonResponse(result_set)

def file_valid(file):
  return True

