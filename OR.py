import csv
import json
import os
from collections import OrderedDict
from io import StringIO
from pprint import pprint
import pandas as pd

from OpenRefineClientPy3.google_refine.refine import refine
from OpenRefineClientPy3.google_refine.refine import facet


class Refineop(refine.RefineProject):
    # inherit class from RefineProject
    def __init__(self,server, projectID):
        super().__init__(server,projectID)

    def list_history(self):
        return super().list_history()

    def undo_redo_proj(self, lastDone_id,token):
        return super().undo_redo_project(lastDone_id,token)

    # def project_url(self):
    #     # project_url
    #     return super().project_url()

    def do_json(self, command,token=None, data=None, include_engine=True):
        return super().do_json(command, token, data)

    def do_raw(self,command, data):
        # do_raw :  issue a command to the server & return a response object
        return super().do_raw(command, data)

    def get_models(self):
        # get_models: fill out column metadata.
        # Column structure is a list of columns in their order.
        # The cellIndex is an index for that column's data into the list returned from get_rows().
        return super().get_models()

    # def get_cell_value(self,columnIndex, token):
    #     # split break.....
    #     # nestedlist: [{u'cells': [{u'v': u'10136'},....{}]},{u 'cells': [...]}]
    #     # The cellIndex is an index for that column's data into the list returned from get_rows().
    #     # 'from': cell_value, 'to': new_cell_value
    #     nested_list = super().get_cell_value(token)
    #     AimCellValue = []
    #     for inner_dicts in nested_list:
    #         AimCellValue.append(inner_dicts['cells'][columnIndex])
    #     return AimCellValue
    #
    # def get_single_cell_value(self, cellIndex, rowIndex, token):
    #     nested_list = super().get_cell_value(token)
    #     aim_single_cell_value = nested_list[rowIndex]['cells'][cellIndex]
    #     return aim_single_cell_value

    # def get_split_cell_value(self,origin_column_length):
    #     nested_list = super().get_cell_value()
    #     print(len(nested_list))
    #     AimcellValue = []
    #     counter = []
    #     for inner_dicts in nested_list:
    #         if len(inner_dicts['cells']) > origin_column_length:
    #             counter.append(len(inner_dicts['cells']) - origin_column_length - 1)
    #             AimcellValue.append(inner_dicts['cells'][origin_column_length + 1:])
    #     return counter, AimcellValue

    def get_preference(self, name):
        # get preference: returns the (OR_JSON) value of a given preference setting.
        return super().get_preference(name)

    def apply_operations(self, token, file_path, wait=True):
        # apply operations: apply the json file
        return super().apply_operations(token, file_path)

    def export(self, export_format='csv'):
        # export : return a fileobject of a project's data.
        return super().export(export_format)

    def export_rows(self, **kwargs):
        # return an iterable of parsed rows of a project's data
        return super().export_rows(**kwargs)

    def delete(self,token):
        # delete the project
        return super().delete(token)

    def compute_facets(self, token,facets=None):
        return super().compute_facets(token,facets)

    def get_rows(self, token,facets=None, sort_by=None, start=1, limit=100):
        return super().get_rows(token,facets, sort_by, start, limit)

    def reorder_rows(self, token,sort_by=None):
        return super().reorder_rows(token,sort_by)

    def remove_rows(self, token,facets=None):
        return super().remove_rows(token,facets)

    def text_transform(self, column, expression, token, on_error='set-to-blank', repeat=False, repeat_count=10):
        return super().text_transform(column, expression, token,on_error, repeat, repeat_count)

    def compute_clusters(self, column, token,clusterer_type='binning', function=None, params=None):
        # returns a list of cluters of {'value';..., 'count':...}
        return super().compute_clusters(column, token,clusterer_type, function, params)

    '''insert a function to automatically get 'from' '''

    def getFromValue(self,clusters):
        fromlist = []
        fromlistInner = []
        for cluster in clusters:
            for clu in cluster:
                fromlistInner.append(clu['value'])
            fromlist.append(fromlistInner)
            fromlistInner = []
        return fromlist

    '''insert a function to automatically get 'to' '''

    def getToValue(self,clusters):
        result = [
            max(list_of_dicts, key=lambda d: d['count'])
            for list_of_dicts in clusters
        ]
        chosenvaluelist = []
        for chosendict in result:
            chosenvaluelist.append(chosendict['value'])
        return chosenvaluelist

    def edit(self, column, edit_from, edit_to,token):
        return super().edit(column, edit_from, edit_to, token)

    def mass_edit(self, column, edits, token, expression='value'):
        return super().mass_edit(column, edits, token,expression)

    def single_edit(self, row, cell, type, value,token):
        return super().single_edit(row, cell, type, value,token)

    def annotate_one_row(self, row, annotation,token, state=True):
        return super().annotate_one_row(row, annotation,token, state)

    def flag_row(self, row, flagged=True):
        return super().flag_row(row, flagged)

    def star_row(self, row, starred=True):
        return super().star_row(row, starred)

    def add_column(self, column, new_column, token,expression='value', column_insert_index=None, on_error='set-to-blank'):
        return super().add_column(column=column, new_column=new_column, token= token,expression=expression)

    def split_column(self, column, token, separator=',', mode='separator', regex=False, guess_cell_type=True,
                     remove_original_column=True):
        return super().split_column(column, token, separator, mode, regex, guess_cell_type,remove_original_column)

    def rename_column(self, column, new_column,token):
        return super().rename_column(column, new_column,token)

    def reorder_columns(self, new_column_order,token):
        return super().reorder_columns(new_column_order,token)

    def move_column(self, column, index, token):
        return super().move_column(column, index,token)

    def blank_down(self, column,token):
        return super().blank_down(column,token)

    def fill_down(self, column,token):
        return super().fill_down(column,token)

    def transpose_columns_into_rows(self, start_column, column_count,
                                    combined_column_name, token, separator=':', prepend_column_name=True,
                                    ignore_blank_cells=True):
        return super().transpose_columns_into_rows(start_column,column_count, combined_column_name,token,separator, prepend_column_name,ignore_blank_cells)

    def transpose_rows_into_columns(self, column, row_count,token):
        return super().transpose_rows_into_columns(column, row_count,token)

    def guess_types_of_column(self, column, token, service):
        return super().guess_types_of_column(column,token, service)

    def get_reconciliation_services(self):
        return super().get_reconciliation_services()

    def get_reconciliation_service_by_name_or_url(self, name):
        return super().get_reconciliation_service_by_name_or_url(name)

    def reconcile(self, column, token,service, reconciliation_type=None, reconciliation_config=None):
        return super().reconcile(column, token, service, reconciliation_type, reconciliation_config)

    def get_operations(self):
        return super().get_operations()

    def load_ops(self,name):
        ops = self.get_operations()
        with open(f'{name}.json', 'w') as fout:
            json.dump(ops, fout, indent=4)

    def load_data(self, filename):
        with open(filename, 'wb')as f:
            reader = self.export('csv')
            for row in reader:
                f.write(row)


def main():
    # server = refine.RefineServer()
    # orefine = refine.Refine(server)
    projects = refine.Refine(refine.RefineServer()).list_projects()
    pprint(projects)
    p = refine.Refine(refine.RefineServer()).open_project(2014260363969)
    print(p.list_history())
    fr = p.compute_facets(facet.TextFacet('event'))
    facets = fr.facets[0]
    print(facets)
    for k in sorted(facets.choices,
                    key=lambda k: facets.choices[k].count,
                    reverse=True):
        print(facets.choices[k].count, k)

    # server = refine.RefineServer()
    # projectID = 2124203262743
    # refineop = Refineop(server, projectID)
    # history = refineop.list_history()
    # print(history)
    # csrf_t = server.get_csrf()['token']
    # refineop.undo_redo_proj(lastDone_id=1604859434295,token=csrf_t)
    #
    # csrf_t_1 = server.get_csrf()['token']
    # print(csrf_t_1)
    # clusters = refineop.compute_clusters('event', clusterer_type='binning', function='fingerprint')
    # pprint(clusters)
    # from_edit=refineop.getFromValue(clusters)
    # to_edit=refineop.getToValue(clusters)
    # default_edits=OrderedDict()
    # default_edits['fromBlank']='false'
    # default_edits['fromError']='false'
    # for f1,t1 in zip(from_edit, to_edit):
    #     default_edits['from']=f1
    #     default_edits['to']=t1
    # edits=[default_edits]
    # # mass edit : column, edits
    # refineop.mass_edit('Country', edits, csrf_t_1)
    # opening an OpenRefine Project

    # oprefine = Refineop(server,1596601650071)
    # refinesever = refine.RefineServer()

    # refine.Refine(refine.RefineServer()).new_project(token=csrf_t, project_file='CoronaVirus_tweets.csv',project_name='demo_fall2020')

    # p = refine.Refine(refine.RefineServer()).open_project(2014260363969)
    #
    # refinesever =refine.RefineServer()
    # csrf_t = refinesever.get_csrf()['token']
    # csrf_t = refinesever.get_csrf()
    # pprint(csrf_t)
    # facet
    # p.undo_redo_project(1587412700412,csrf_t)
    # fr = p.compute_facets(facet.TextFacet('Country'))
    # facets = fr.facets[0]
    # for k in sorted(facets.choices,
    #                 key=lambda k: facets.choices[k].count,
    #                 reverse=True):
    #     print(facets.choices[k].count, k)



    # KEY = list(orefine.list_projects().keys())[0]
    # print(KEY)
    # # 2014260363969
    # p = orefine.open_project(KEY)
    # print(p.columns)
    # pd.read_csv(StringIO (p.export(export_format='csv')))




    # oprefine = Refineop(server,projectID= KEY)


    # proj_name = refine.Refine(server).get_project_name(1596601650071)
    # print(proj_name)
    # cells = oprefine.get_single_cell_value(4,1)
    # oprefine.single_edit(27, 5, 'text', 'KIMBA707')
    # cur_op = oprefine.get_operations()
    # pprint(cur_op)
    # oprefine.flag_row(1)
    # oprefine.load_ops('test')
    # oprefine.load_data('clean.csv')


if __name__ == '__main__':
    main()

