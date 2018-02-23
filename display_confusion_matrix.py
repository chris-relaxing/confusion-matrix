
def display_confusion_matrix(data):
    """Display confusion matrix in a nice table."""
    data_prep = [['<center><b>True Negative</b><br><br>','<center><b>False Positive</b><br><br>'],
                 ['<center><b>False Negative</b><br><br>','<center><b>True Positive</b><br><br>']]
    
    print_data = [[data_prep[0][0]+str(data[0][0]), data_prep[0][1]+str(data[0][1])],
                  [data_prep[1][0]+str(data[1][0]), data_prep[1][1]+str(data[1][1])]]
    display(HTML(
    '<table><tr>{}</tr></table>'.format(
        '</tr><tr align="center">'.join(
            '<td width="150" align="center">{}</td>'.format('</td><td width="150" align="center">'.join(str(_) for _ in row)) for row in print_data)
        )
    ))