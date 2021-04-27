from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from comments.models import Comment
from comments.serializers import CommentSerializer

@api_view(['GET','POST'])
def blog_list(request):
    if(request.method == 'GET'):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','PUT','DELETE'])
def blog_detail(request,pk,format=None):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        comments = Comment.objects.filter(blog=pk)
        serializer2 = CommentSerializer(comments, many=True)
        data = {
            "blog": serializer.data,
            "comments": serializer2.data
        }
        return Response(data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = BlogSerializer(data=request.data)
        if status.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        blog.delete() 
        return Response(status.HTTP_204_NO_CONTENT)   
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)