from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from service_application_package import db
from service_application_package.models import Story
from service_application_package.stories.forms import StoryForm

stories = Blueprint('stories', __name__)


# 
# Stories
# 
@stories.route("/projects/<int:project_id>/requirements/<int:requirement_id>/stories/new", methods=['GET', 'POST'])
@login_required
def new_story(project_id, requirement_id):
    form = StoryForm()
    if form.validate_on_submit():
        story = Story(title=form.title.data
                    , content=form.content.data
                    , project_id=project_id
                    ,requirement_id=requirement_id
                    ,status=form.status.data
                    ,assigned_to=form.assigned_to.data)
        db.session.add(story)
        db.session.commit()
        flash('Your story has been created!', 'success')
        return redirect(url_for('stories.list_stories', project_id=project_id, requirement_id=requirement_id))
    return render_template('create_story.html', title='New story',
                           form=form, legend='New story')

@stories.route("/projects/<int:project_id>/requirement/<int:requirement_id>/stories/<int:story_id>")
def story(project_id, requirement_id, story_id):
    story = Story.query.get_or_404(story_id)
    return render_template('stories.html', title=story.title, story=story, project_id=project_id, requirement_id=requirement_id)


@stories.route("/projects/<int:project_id>/requirements/<int:requirement_id>/stories/all")
def list_stories(project_id,requirement_id):
    form = StoryForm()
    story_count = Story.query.filter_by(requirement_id=requirement_id).count()
    if story_count > 0:
        stories = Story.query.filter_by(requirement_id=requirement_id)
    else:
        stories = 0
    return render_template('stories.html', 
                           form=form, title='story', legend="New story", stories=stories, project_id=project_id, requirement_id=requirement_id)


@stories.route("/projects/<int:project_id>/requirements/<int:requirement_id>/stories/<int:story_id>", methods=['GET', 'POST'])
def add_story(project_id, requirement_id, story_id):    
    story = Story.query.get_or_404(story_id)
    form = StoryForm()
    if form.validate_on_submit():
        story = Story(title=form.title.data
                , content=form.content.data
                , project_id=project_id
                , requirement_id=requirement_id
                , status=form.content.status)        
        db.session.add(story)
        db.session.commit()
        flash('Your story has been created!', 'success')
        return redirect(url_for('stories.list_stories'))
    return render_template('stories.html', title='New story',
                           form=form, legend='New story', requirement_id=requirement.id, project_id=project.id, story=story.id)


@stories.route("/projects/<int:project_id>/requirements/<int:requirement_id>/stories/<int:story_id>/update", methods=['GET', 'POST'])
@login_required
def update_story(project_id, requirement_id, story_id):
    story = Story.query.get_or_404(story_id)
    form = StoryForm()
    if form.validate_on_submit():
        story.title = form.title.data
        story.content = form.content.data
        story.status = form.status.data
        story.assigned_to = form.assigned_to.data
        db.session.commit()
        flash('Your story has been updated!', 'success')
        return redirect(url_for('stories.list_stories', requirement_id=requirement_id, project_id=project_id, story=story.id))
    elif request.method == 'GET':
        form.title.data = story.title
        form.content.data = story.content
        form.status.data = story.status
    return render_template('create_story.html', title='Update story',
                           form=form, legend='Update story')

@stories.route("/projects/<int:project_id>/requirements/<int:requirement_id>/stories/<int:story_id>/delete", methods=['POST'])
@login_required
def delete_story(project_id, requirement_id,story_id):
    story = Story.query.get(story_id)
    db.session.delete(story)
    db.session.commit()
    flash('Your story has been deleted!', 'success')
    return redirect(url_for('stories.list_stories', project_id=project_id,requirement_id=requirement_id))