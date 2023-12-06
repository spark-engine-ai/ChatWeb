import React from 'react';
interface GridSectionProps {
  title: string;
  gridLayout: string;
}
const GridSection: React.FC<GridSectionProps> = ({ title, gridLayout }) => {
  const gridItems = [
    { id: 1, image: 'image1.jpg', title: 'Item 1' },
    { id: 2, image: 'image2.jpg', title: 'Item 2' },
    { id: 3, image: 'image3.jpg', title: 'Item 3' },
    { id: 4, image: 'image4.jpg', title: 'Item 4' },
    { id: 5, image: 'image5.jpg', title: 'Item 5' },
    { id: 6, image: 'image6.jpg', title: 'Item 6' },
  ];
  return (
    <div>
      <h2 className="text-center text-3xl font-bold text-white">{title}</h2>
      <div className={`grid grid-cols-${gridLayout}`}>
        {gridItems.map((item) => (
          <div key={item.id} className="p-4">
            <img src={item.image} alt={item.title} />
            <p className="text-white">{item.title}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
export default GridSection;