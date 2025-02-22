from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    '''The home page for learning log'''
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # #to make sure the topic belong to current user

    
    # context = {
    #     'topics': topics
    # }
    return render(request, 'learning_logs/index.html')

#creating the topics view
@login_required
def topics(request):
    '''The topic page for learning log'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    #to make sure the topic belong to current user

    
    context = {
        'topics': topics
    }
    return render(request,'learning_logs/topics.html',context)
#creating the topic to view entries
@login_required
def topic(request,topic_id):
    '''Rrturning the entries regarding the topic'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    if topic.owner != request.user:
        raise Http404

  
    context = {
        'entries':entries,
        'topic_id':topic_id,
        'Title':topic.text,
    }
    return render(request,'learning_logs/topic.html',context)

#for adding new topic
@login_required
def newTopics(request):
    '''For adding new topics'''
    if request.method != 'POST':
        #no data submitted; create a blank form.
        form = TopicForm()
    else:
        #POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form':form}

    return render(request,'learning_logs/newTopics.html',context)

@login_required
def newEntry(request,topic_id):
    '''For adding new Entry'''
    topic = Topic.objects.get(id = topic_id)
    
    if request.method != 'POST':
        #no data submitted; create a blank form
        form = EntryForm()
    else:
        #Post data submitted,process data
        form = EntryForm(data = request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    
    context = {
        'form':form,
        'topic_id':topic_id,
        'title':topic.text
    }
    return render(request,'learning_logs/newEntry.html',context)
@login_required
def editEntry(request,entry_id):
    '''To edit the entry'''
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    #editing by open the entry form
    if request.method != 'POST':
        #initializing the form with current entry
        form = EntryForm(instance= entry)
    else:
        form = EntryForm(instance = entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {
        'entry':entry,
        'form':form,
        'topic':topic,
    }

    return render(request,'learning_logs/editEntry.html',context)
@login_required
def deletEntry(request,entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    entry.delete()
    return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
@login_required  
def deleteTopic(request,topic_id):
    topic = Topic.objects.get(id= topic_id)
    topic.delete()
    return HttpResponseRedirect(reverse('learning_logs:topics'))
