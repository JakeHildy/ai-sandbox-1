import { Box } from '@mui/material';
import PieChartComponent from './PieChartComponent';
import TableComponent from './TableComponent';

// PieChartComponent prop structure
// {
//     "type": "Graph",
//     "props": {
//         "labels": ["January", "February", "March", "April", "May"],
//         "datasets": [
//             {
//                 "data": [3000, 4500, 5000, 6000, 7000],
//                 "backgroundColor": "#3e95cd"
//             }
//         ]
//     }
// }

// TableComponent prop structure
// {
//     "columns": ["Name", "Age", "Country"],
//     "data": [
//         {"Name": "John", "Age": "30", "Country": "USA"},
//         {"Name": "Mike", "Age": "25", "Country": "Canada"},
//         {"Name": "Sue", "Age": "35", "Country": "Australia"}
//     ]
// }

const Example = () => {
    const graphProps = {
        labels: ["January", "February", "March", "April", "May"],
        datasets: [
            {
                data: [3000, 4500, 5000, 6000, 7000],
                backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"]
            }
        ]
    };

    const tableProps = {
        columns: ["Name", "Age", "Country"],
        data: [
            {"Name": "John", "Age": "30", "Country": "USA"},
            {"Name": "Mike", "Age": "25", "Country": "Canada"},
            {"Name": "Sue", "Age": "35", "Country": "Australia"}
        ]
    };

    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
            <TableComponent columns={tableProps.columns} data={tableProps.data} />
            <PieChartComponent data={graphProps} sx={{border: '1px solid red'}}/>
        </Box>
    );
};

export default Example;
