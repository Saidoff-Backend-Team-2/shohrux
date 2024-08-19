from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
import os


class Media(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = 'image', _('Image')
        VIDEO = 'video', _("Video")
        AUDIO = 'audio', _('Audio')
        OTHER = 'other', _("Other")

    file = models.FileField(_('file'), upload_to='all_media_files/')
    type = models.CharField(_('type'), max_length=20, choices=MediaType.choices, default=MediaType.IMAGE)

    def __str__(self):
        return f"{self.file.name}-{self.type}"

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Medias')

    def clean(self):
        ext = os.path.splitext(self.file.name)[1][1:].lower()
        allowed_extensions = {
            Media.MediaType.IMAGE: ['jpg', 'jpeg', 'png'],
            Media.MediaType.VIDEO: ['mp4'],
            Media.MediaType.AUDIO: ['mp3'],
            Media.MediaType.OTHER: [],
        }

        if self.type in allowed_extensions and ext not in allowed_extensions[self.type]:
            raise ValidationError(
                _(f'Only {", ".join(allowed_extensions[self.type])} are allowed for {self.type} files!'))
