
#from openerp import models, fields, api
from openerp.osv import fields, osv

class openexams_exam(osv.Model):
    _name = 'openexams.exam'
    _columns = {
        'name' : fields.char(string="SEM:INTERNAL:YEAR"),
        'course' : fields.many2one('openexams.course','Course'),
        'internal': fields.integer(string="Internal", required=True),
        'sem':  fields.selection(
            [('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'), ('8', 'S8')],
            'Semester', default="normal", required=True),
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
        'sem':  fields.selection(
            [('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'), ('8', 'S8')],
            'Semester', default="normal", required=True),
        'discription': fields.text(string="Discription")
    }

class openexams_co_po(osv.Model):
    _name = 'openexams.co.po'
    _columns = {
        'weight': fields.selection(
            [('1', 'LOW'), ('2', 'MED'), ('3', 'HIGH')],
            'Weight', default="normal", required=True),
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
