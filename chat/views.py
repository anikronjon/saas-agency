from django.shortcuts import render, redirect
from .forms import ChatGroup


def message_group_view(request):
    if request.method == 'POST':
        form = ChatGroup(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            return redirect('chat:chat_page', group_name=group_name)
    else:
        form = ChatGroup()
    return render(request, 'chat/group.html', {'form': form})


def message_chat_view(request, group_name):
    return render(request, 'chat/chat.html', {'group_name': group_name})

