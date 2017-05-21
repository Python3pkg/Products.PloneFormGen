from Products.Five import BrowserView

HAS_RECAPTCHA = True
try:
    from collective.recaptcha.settings import RecaptchaSettingsForm
except ImportError:
    HAS_RECAPTCHA = False

if HAS_RECAPTCHA:

    class CaptchaControlPanel(RecaptchaSettingsForm):
        description = 'The PloneFormGen captcha field is based on the Recaptcha service. To use it ' + \
                      'you must obtain an account at recaptcha.net, generate keys for this site, and ' + \
                      'enter them here. '

        has_recaptcha = True

else:

    class CaptchaControlPanel(BrowserView):
        has_recaptcha = False
