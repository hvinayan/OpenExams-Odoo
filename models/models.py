
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

class openexams_mark(osv.Model):
    _name = 'openexams.mark'
    _columns = {
        'studentid' :  fields.many2one('students.student','Student',required=True),
        'examid' : fields.many2one('openexams.exam','Exam',required=True),
        'question' : fields.integer(string="Question Number",required=True),
        'marks' : fields.integer(string="Marks Obtained",required=True),
        'maxmarks' : fields.integer(string="Max Marks",required=True),
        'coid' : fields.many2one('openexams.co','CO',required=True)
    }

    def copy_mark(self, cr, uid, ids, context=None):
        for rec in self.browse(cr, uid, ids, context):
            self.copy(cr,uid, rec.id , {},context)
        return True

class openexams_po(osv.Model):
    _name = 'openexams.po'
    _columns = {
        'name': fields.char(string="PO" , required=True),
        'discription': fields.text(string="Discription")
    }

class openexams_course(osv.Model):
    _name = 'openexams.course'
    _columns = {
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
        'name': fields.char(string="Name" , required=True),
        'discription': fields.text(string="Discription"),
        'courseid': fields.many2one('openexams.course','Course'),
        'po_id' : fields.many2many('openexams.po','openexams_co_po','co_id','po_id', string='POs Related')
    }
