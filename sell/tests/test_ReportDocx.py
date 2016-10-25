# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.addons.report_docx.report.report_docx import DataModelProxy
from odoo.tools import misc
import random,os

class test_ReportDocx(TransactionCase):

    def setUp(self):
        '''准备数据'''
        super(test_ReportDocx, self).setUp()
        self.ir_actions = self.env.ref('sell.report_sell_order_1')
        self.sell_order = self.env.ref('sell.sell_order_1')
        self.report_docx_sell = self.ir_actions._lookup_report('sell.order')

        self.ir_actions = self.env.ref('sell.report_sell_order_2')
        self.sell_order = self.env.ref('sell.sell_order_1')
        self.report_pdf_sell = self.ir_actions._lookup_report('sell.order')


    def test_lookup_report(self):
        '''测试docx报表模板'''
        self.report_docx_sell.create(self.cr, self.uid, self.sell_order.id, self.ir_actions, self.env.context)

    def test_lookup_report_pdf(self):
        '''测试docx报表模，输出类型为pdf'''
        self.ir_actions.write({'output_type':'pdf'})
        self.report_docx_sell.create(self.cr, self.uid,self.sell_order.id, self.ir_actions, self.env.context)

    def test_get_docx_data(self):
        model = self.report_docx_sell.get_docx_data(self.cr, self.uid, self.ir_actions.id, self.ir_actions, self.env.context)

    def test_save_file(self):
        doxc_file = self.report_docx_sell.create(self.cr, self.uid, self.sell_order.id, self.ir_actions, self.env.context)
        self.report_docx_sell._save_file(misc.file_open('sell/tests/sell.order.docx').name,doxc_file)

    # def test_render_to_pdf(self):
    #     self.report_pdf_sell.render_to_pdf( os.path.join(os.getcwd(), 'temp_%s_%s.%s' %
    #                         (os.getpid(), random.randint(1, 10000), 'docx')))

    def test_datamodelproxy(self):
        data=DataModelProxy([{"type":'selection'}])
        data.__getitem__(0)
        data = DataModelProxy([])
        data.__getattr__(0)