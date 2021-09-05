from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import StudentForm
from .models import Student
from django.views.generic import View, CreateView,  ListView,  UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


class StudentInfo(CreateView):
    model = Student
    fields = ('st_id','name', 'age', 'Sex', 'fatherName', 'motherName', 'lastEducation')
    template_name = 'student_form.html'

    def form_valid(self, form):
        student = form.save(commit=False)
        student.save()
        return HttpResponseRedirect(reverse('student_info:student_list'))


class ListPage(ListView):
    context_object_name = 'student'
    model = Student
    template_name = 'student_view.html'


class EditPage(UpdateView):
    fields = ('st_id', 'name', 'age', 'Sex', 'fatherName', 'motherName', 'lastEducation')
    model = Student
    template_name = 'edit_student.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('student_info:student_list', kwargs={})


class DeletePage(DeleteView):
    context_object_name = 'student'
    model = Student
    template_name = 'delete_student.html'
    success_url = reverse_lazy('student_info:student_list')


class StudentDetail(DetailView):
    context_object_name = 'student'
    model = Student
    template_name = 'student_details.html'

