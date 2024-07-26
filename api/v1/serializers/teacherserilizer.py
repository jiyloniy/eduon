from rest_framework import serializers
from apps.users.models import Teacher,Experiences
from api.v1.serializers.userserializer import UserSerializer

class ExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiences
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    experience = ExperiencesSerializer(many=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        try:
            user_data = validated_data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            user.set_password(user_data.get('password'))
            user.save()
            experience_data = validated_data.pop('experience')
            experience = [ExperiencesSerializer.create(ExperiencesSerializer(), validated_data=exp_data) for exp_data in experience_data]
            teacher = Teacher.objects.create(user=user, **validated_data)
            teacher.experience.set(experience)
            return teacher
        except Exception as e:
            user.delete()
            raise e
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user = UserSerializer.update(UserSerializer(), user, user_data)
        experience_data = validated_data.pop('experience')
        for exp_data in experience_data:
            experience_instance = instance.experience.get(id=exp_data.get('id'))
            experience_instance.company = exp_data.get('company', experience_instance.company)
            experience_instance.title = exp_data.get('title', experience_instance.title)
            experience_instance.description = exp_data.get('description', experience_instance.description)
            experience_instance.position = exp_data.get('position', experience_instance.position)
            experience_instance.start_date = exp_data.get('start_date', experience_instance.start_date)
            experience_instance.end_date = exp_data.get('end_date', experience_instance.end_date)
            experience_instance.save()
        instance.save()
        return instance
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserSerializer(instance.user).data
        rep['experience'] = ExperiencesSerializer(instance.experience.all(), many=True).data
        request = self.context.get('request',None)
        if request and (request.user.is_anonymous or request.user.user_type not in [1,4]):
            if 'username' in rep['user']:
                rep['user'].pop('username')
            if 'last_login' in rep['user']:
                rep['user'].pop('last_login')
            
            if 'is_superuser' in rep['user']:
                rep['user'].pop('is_superuser')
            
            if 'is_staff' in rep['user']:
                rep['user'].pop('is_staff')
            
            if 'user_type' in rep['user']:
                rep['user'].pop('user_type')
            if 'groups' in rep['user']:
                rep['user'].pop('groups')
            
            if 'user_permissions' in rep['user']:
                rep['user'].pop('user_permissions')
            
            if 'password' in rep['user']:
                rep['user'].pop('password')
        if request and request.user.user_type  in [1,4]:        
            if 'password' in rep['user']:
                rep['user'].pop('password')
        return rep
    
    def to_internal_value(self, data):
        data['user'] = UserSerializer().to_internal_value(data.get('user', {}))
        data['experience'] = ExperiencesSerializer(many=True).to_internal_value(data.get('experience', []))
        return super().to_internal_value(data)