from django.contrib import admin
from .models import AssociacaoEntreConvenios, AtividadeProjeto, Cargo, \
                    Colaborador, ColaboradorProjeto, Convenio, DicionarioErro, \
                    DicionarioSucesso, \
                    Equipamento, EquipamentoProjeto, GastoConvenio, \
                    GastoProjeto, IncidenciasColaborador, \
                    Projeto, TipoEquipamento


class AssociacaoEntreConveniosAdmin(admin.ModelAdmin):
    pass

admin.site.register(AssociacaoEntreConvenios, AssociacaoEntreConveniosAdmin)

class AtividadeProjetoAdmin(admin.ModelAdmin):
    pass
admin.site.register(AtividadeProjeto, AtividadeProjetoAdmin)