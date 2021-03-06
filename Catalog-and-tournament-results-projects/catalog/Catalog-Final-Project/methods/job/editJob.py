from flask import render_template, url_for, flash, request, redirect
from methods import routes
from helpers import sessionMaker
from database_setup import Job, Category
from helpers import permissions

session = sessionMaker.newSession()


@routes.route('/employer/<int:employer_id>/job/<int:job_id>/edit',
              methods=['GET', 'POST'])
def editJob(employer_id, job_id):
    categories = session.query(Category).all()
    i = session.query(Job).filter_by(id=job_id).one()

    if request.method == 'POST':
        if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
            if request.form['header']:
                i.header = request.form['header']
                i.salary = request.form['salary']
                i.description = request.form['description']
                i.category_id = request.form['category']
                session.add(i)
                session.commit()
                flash("You got it! Job updated.")
                return redirect(url_for('routes.viewEmployer',
                                        employer_id=employer_id))
        else:
            flash("You don't have permission to do this.")
            return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))
    else:
        if permissions.EmployerAdminAndLoggedIn(employer_id) == True:
            return render_template(
                '/job/editjob.html', employer_id=employer_id,
                job_id=job_id, job=i, categories=categories)
        else:
            flash("You don't have permission to do this.")
            return redirect(url_for('routes.viewEmployer',
                                    employer_id=employer_id))

# Possible future functions
# Batch edit
# More advanced edit handling ie images
