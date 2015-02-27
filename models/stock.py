from openerp.osv import osv, fields

class StockPicking(osv.osv):
    _inherit = 'stock.picking'
    _columns = {
        'purchase_notes': fields.related('purchase', 'notes', string='Purchase Notes', type="text"),
	'sale_notes': fields.related('sale_id', 'note', string='Sale Notes', type="text"),
    }
