from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
<<<<<<< HEAD
from rest_framework.validators import UniqueTogetherValidator
from posts.models import Comment, Post, Follow, User, Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('following',)
=======


from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post
>>>>>>> d048caee5710575b414ec6420ab257c1e663aeda


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
<<<<<<< HEAD
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        exclude = ('id',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return value
=======
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
>>>>>>> d048caee5710575b414ec6420ab257c1e663aeda
