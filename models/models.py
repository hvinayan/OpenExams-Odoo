# -*- coding: utf-8 -*-

#from openerp import models, fields, api
from openerp.osv import fields, osv

class openexams_questionpaper(osv.Model):
    _name = 'openexams.questionpaper'
    _columns = {
        'internal': fields.integer(string="Internal", required=True),
        'sem': fields.integer(string="Semester"),
        'date': fields.date('Conducted on')
    }
class openexams_po(osv.Model):
    _name = 'openexams.po'
    _columns = {
        #'po_id': fields.integer(string="ID", required=True),
        'name': fields.char(string="PO" , required=True),
        'discription': fields.text(string="Discription")
    }

class openexams_course(osv.Model):
    _name = 'openexams.course'
    _columns = {
        #'po_id': fields.integer(string="ID", required=True),
        'name': fields.char(string="Name" , required=True),
        'discription': fields.text(string="Discription")
    }

class openexams_co_po(osv.Model):
    _name = 'openexams.co.po'
    _columns = {
        'name'  : fields.char(string="Name"),
        'weight': fields.integer(string="Weight"),
        'co_id' : fields.many2one('openexams.co','CO'),
        'po_id' : fields.many2one('openexams.po','PO')
    }


class openexams_co(osv.Model):
    _name = 'openexams.co'
    _columns = {
        #'co_id': fields.integer(string="ID", required=True),
        'name': fields.char(string="Name" , required=True),
        'discription': fields.text(string="Discription"),
        'courseid': fields.many2one('openexams.course','Course'),
        'po_id' : fields.many2many('openexams.po','openexams_co_po','co_id','po_id', string='POs Related')
    }


    #semester = fields.Integer()
    #date = fields.date('Exam Date')
    #discription = fields.Text()3

# class openexams(models.Model):
#     _name = 'openexams.openexams'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
