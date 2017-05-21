from zope.i18n import translate
from zope.publisher.browser import BrowserView

from Products.CMFCore.utils import getToolByName
from Products.PloneFormGen import PloneFormGenMessageFactory as _

# Creates a javascript variable view with the format:
# pfgQEdit.messages = {
# FIELD_MSG: 'Field',
# ACTIONS_MSG: 'Actions',
# ORDER_MSG: 'Order'}
#
# To add a message, just put it in the messages dict

messages = {
    'ORDER_MSG' : _('order', default='Order'),
    'FIELD_MSG' : _('field', default='Field'),
    'ACTIONS_MSG' : _('actions', default='Actions'),
    'NO_CAPTCHA_MSG' : _('no_captcha_msg', default='Captcha field hidden by form editor. Refresh to view it.'),
    'AJAX_FAILED_MSG' : _('ajax_failed_msg', 'Unable to load resource: '),
    'MORE_FIELDS_MSG' : _('more_fields_msg', 'More fields...'),
    'LESS_FIELDS_MSG' : _('less_fields_msg', "Less fields..."),

}

messageTemplate = "pfgQEdit_messages = {\n%s}\n"

class JSVariables(BrowserView):

    def __call__(self, *args, **kwargs):
        context = self.context
        response = self.request.response
        response.setHeader('content-type','text/javascript;;charset=utf-8')

        template = ''

        for key in messages:
            msg = translate(messages[key], context=self.request).replace("'", "\\'")
            template = "%s%s: '%s',\n" % (template, key, msg)

        # note trimming of last comma
        return messageTemplate % template[:-2]
