/* eslint-disable react/prop-types */
import { Box, Typography } from '@mui/material'
import TableComponent from './TableComponent'
import PieChartComponent from './PieChartComponent'


const Results = ({responseObj}) => {

    console.log(responseObj);
    return <>
        <Typography variant="h5" component="h2" gutterBottom>Results</Typography>
        {responseObj && <ComponentFactory componentDescription={responseObj} />}
    </>
    
}


const ComponentFactory = ({ componentDescription }) => {
    const { type, props, children } = componentDescription;

    if (type === 'Typography') {
        return <Typography {...props}>{children}</Typography>;
    } else if (type === 'Box') {
        return <Box {...props}>{children && children.map((child, index) => <ComponentFactory key={index} componentDescription={child} />)}</Box>;
    } else if (type === 'Table') {
        return <TableComponent {...props}>{children}</TableComponent>;
    } else if (type === 'PieChart') {
        return <PieChartComponent {...props}>{children}</PieChartComponent>;
    }
    // Add more component types as needed
    return null;
};

export default Results

// {
//     type: 'Graph',
//     props: { 
//         labels: ['January', 'February', 'March', 'April', 'May'],
//         datasets: [
//             { data: [2000, 2500, 1800, 3000, 2800], backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#00b894', '#6c5ce7'] } 
//         ] 
//     }
// }