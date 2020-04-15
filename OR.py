import json
import os
from pprint import pprint

from OpenRefineClientPy3.google_refine.refine import refine


class Refineop(refine.RefineProject):
    # inherit class from RefineProject
    def __init__(self,server, projectID):
        super().__init__(server,projectID)

    def list_history(self):
        return super().list_history()

    def undo_proj(self, lastDone_id):
        return super().undo_project(lastDone_id)

    # def project_url(self):
    #     # project_url
    #     return super().project_url()
    def do_json(self, command, data=None, include_engine=True):
        return super().do_json(command, data)

    def do_raw(self,command, data):
        # do_raw :  issue a command to the server & return a response object
        return super().do_raw(command, data)

    def get_models(self):
        # get_models: fill out column metadata.
        # Column structure is a list of columns in their order.
        # The cellIndex is an index for that column's data into the list returned from get_rows().
        return super().get_models()

    def get_cell_value(self,columnIndex):
        # split break.....
        # nestedlist: [{u'cells': [{u'v': u'10136'},....{}]},{u 'cells': [...]}]
        # The cellIndex is an index for that column's data into the list returned from get_rows().
        # 'from': cell_value, 'to': new_cell_value
        nested_list = super().get_cell_value()
        AimCellValue = []
        for inner_dicts in nested_list:
            AimCellValue.append(inner_dicts['cells'][columnIndex])
        return AimCellValue

    def get_single_cell_value(self, cellIndex, rowIndex):
        nested_list = super().get_cell_value()
        aim_single_cell_value = nested_list[rowIndex]['cells'][cellIndex]
        return aim_single_cell_value

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

    def apply_operations(self, file_path, wait=True):
        # apply operations: apply the json file
        return super().apply_operations(file_path)

    def export(self, export_format='tsv'):
        # export : return a fileobject of a project's data.
        return super().export(export_format)

    def export_rows(self, **kwargs):
        # return an iterable of parsed rows of a project's data
        return super().export_rows(**kwargs)

    def delete(self):
        # delete the project
        return super().delete()

    def compute_facets(self, facets=None):
        return super().compute_facets(facets)

    def get_rows(self, facets=None, sort_by=None, start=1, limit=100):
        return super().get_rows(facets, sort_by, start, limit)

    def reorder_rows(self, sort_by=None):
        return super().reorder_rows(sort_by)

    def remove_rows(self, facets=None):
        return super().remove_rows(facets)

    def text_transform(self, column, expression, on_error='set-to-blank', repeat=False, repeat_count=10):
        return super().text_transform(column, expression, on_error, repeat, repeat_count)

    def compute_clusters(self, column, clusterer_type='binning', function=None, params=None):
        # returns a list of cluters of {'value';..., 'count':...}
        return super().compute_clusters(column, clusterer_type, function, params)

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

    def edit(self, column, edit_from, edit_to):
        return super().edit(column, edit_from, edit_to)

    def mass_edit(self, column, edits, expression='value'):
        return super().mass_edit(column, edits, expression)

    def single_edit(self, row, cell, type, value):
        return super().single_edit(row, cell, type, value)

    def annotate_one_row(self, row, annotation, state=True):
        return super().annotate_one_row(row, annotation, state)

    def flag_row(self, row, flagged=True):
        return super().flag_row(row, flagged)

    def star_row(self, row, starred=True):
        return super().star_row(row, starred)

    def add_column(self, column, new_column, expression='value', column_insert_index=None, on_error='set-to-blank'):
        return super().add_column(column=column, new_column=new_column, expression=expression)

    def split_column(self, column, separator=',', mode='separator', regex=False, guess_cell_type=True,
                     remove_original_column=True):
        return super().split_column(column, separator, mode, regex, guess_cell_type,remove_original_column)

    def rename_column(self, column, new_column):
        return super().rename_column(column, new_column)

    def reorder_columns(self, new_column_order):
        return super().reorder_columns(new_column_order)

    def move_column(self, column, index):
        return super().move_column(column, index)

    def blank_down(self, column):
        return super().blank_down(column)

    def fill_down(self, column):
        return super().fill_down(column)

    def transpose_columns_into_rows(self, start_column, column_count,
                                    combined_column_name, separator=':', prepend_column_name=True,
                                    ignore_blank_cells=True):
        return super().transpose_columns_into_rows(start_column,column_count, combined_column_name,separator, prepend_column_name,ignore_blank_cells)

    def transpose_rows_into_columns(self, column, row_count):
        return super().transpose_rows_into_columns(column, row_count)

    def guess_types_of_column(self, column, service):
        return super().guess_types_of_column(column, service)

    def get_reconciliation_services(self):
        return super().get_reconciliation_services()

    def get_reconciliation_service_by_name_or_url(self, name):
        return super().get_reconciliation_service_by_name_or_url(name)

    def reconcile(self, column, service, reconciliation_type=None, reconciliation_config=None):
        return super().reconcile(column, service, reconciliation_type, reconciliation_config)

    def get_operations(self):
        return super().get_operations()


def main():
    server = refine.RefineServer()
    oprefine = Refineop(server,2014260363969)
    # cells = oprefine.get_single_cell_value(4,1)
    oprefine.flag_row(1)


if __name__ == '__main__':
    main()

