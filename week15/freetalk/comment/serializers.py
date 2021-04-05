from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "body", "author_id", "article_id", "create_time", "update_time")
        read_only_fields = ["id", "author_id", "create_time", "update_time"]
        actions_readonly_fields = {
            ('update', 'partial_update'): ('article_id',)
        }
        
    def get_extra_kwargs(self):
        super(CommentSerializer, self).get_extra_kwargs()
        extra_kwargs = super(CommentSerializer, self).get_extra_kwargs()
        action = self.context['view'].action
        actions_readonly_fields = getattr(self.Meta, 'actions_readonly_fields', None)
        if actions_readonly_fields:
            for actions, fields in actions_readonly_fields.items():
                if action in actions:
                    for field in fields:
                        if extra_kwargs.get(field):
                            extra_kwargs[field]['read_only'] = True
                        else:
                            extra_kwargs[field] = {'read_only': True}
        return extra_kwargs
