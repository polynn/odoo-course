from odoo import fields,models
class CourseLineItem(models.Model):
    _name = "training_center.course.line.item"
    _description = "Course Line Item"
    # String Fields
    name = fields.Char("Content")
    duration = fields.Integer("Duration")
    course_id = fields.Many2one("training_center.course")
    