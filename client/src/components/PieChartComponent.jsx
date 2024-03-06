/* eslint-disable react/prop-types */
import { Box } from '@mui/material';
import { PieChart, Pie, Tooltip, Legend, ResponsiveContainer, Cell } from 'recharts';

const PieChartComponent = (props) => {
  const {datasets, labels} = props;
  const formattedData = labels.map((label, index) => ({
    name: label,
    value: datasets[0].data[index]
  }));

  const COLORS = datasets[0].backgroundColor;

  return (
    <Box sx={{ width: '100%', height: '100%', border: '1px solid #555' }}>
      <ResponsiveContainer width="100%" height={420}>
        <PieChart>
          <Pie
            data={formattedData}
            cx="50%"
            cy="50%"
            labelLine={false}
            outerRadius={80}
            fill="#8884d8"
            dataKey="value"
            label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
          >
            {formattedData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </Box>
  );
};

export default PieChartComponent


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