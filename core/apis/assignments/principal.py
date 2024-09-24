from flask import Blueprint
from core.apis import decorators
from core import db
from .schema import AssignmentSchema, AssignmentSubmitSchema, TeacherSchema,  AssignmentGradeSchema
from core.models.assignments import Assignment
from core.apis.responses import APIResponse
from core.models.teachers import Teacher


principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    principal_assignments = Assignment.get_all_assigments()
    principal_assignments_dums = AssignmentSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=  principal_assignments_dums)

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of Teacher"""
    principal_assignments = Teacher.get_all_teachers()
    principal_assignments_dums = TeacherSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=  principal_assignments_dums)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
